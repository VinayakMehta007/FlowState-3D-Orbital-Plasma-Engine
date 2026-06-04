import pygame
import random
import math
import threading
from ai_agent import get_physics_parameters

# --- Advanced Engine Configuration ---
WIDTH, HEIGHT = 1200, 800
PARTICLE_COUNT = 900  
FPS = 60

# --- Perfected Hollywood Cinematic Themes ---
THEMES = {
    "stark": {
        "name": "TEN RINGS / STARK INDUSTRIES",
        "colors": [[170, 5, 5], [251, 202, 3], [185, 125, 16], [106, 12, 11]], 
        "bg": (6, 2, 3),
        "reticle": (251, 202, 3)
    },
    "spiderverse": {
        "name": "EARTH-1610 (SPIDER-VERSE)",
        "colors": [[240, 113, 103], [131, 56, 236], [29, 53, 87], [230, 57, 70]], 
        "bg": (4, 3, 12),
        "reticle": (240, 113, 103)
    },
    "interstellar": {
        "name": "GARGANTUA ACCRETION DISK",
        "colors": [[255, 180, 80], [50, 120, 255], [255, 220, 150]], 
        "bg": (2, 2, 4),
        "reticle": (255, 180, 80)
    },
    "oppenheimer": {
        "name": "TRINITY CORE (OPPENHEIMER)",
        "colors": [[255, 60, 0], [255, 180, 20], [200, 10, 0]], 
        "bg": (10, 3, 0),
        "reticle": (255, 180, 20)
    },
    "avatar": {
        "name": "PANDORA BIOLUMINESCENCE",
        "colors": [[0, 255, 180], [20, 50, 255], [180, 0, 255]], 
        "bg": (0, 6, 12),
        "reticle": (0, 255, 180)
    },
    "matrix": {
        "name": "THE MATRIX (DIGITAL RAIN)",
        "colors": [[0, 255, 70], [0, 150, 40], [100, 255, 150]], 
        "bg": (0, 5, 2),
        "reticle": (0, 255, 70)
    },
    "tron": {
        "name": "TRON LEGACY (THE GRID)",
        "colors": [[0, 240, 255], [255, 0, 200], [0, 100, 255]], 
        "bg": (5, 0, 15),
        "reticle": (0, 240, 255)
    },
    "dune": {
        "name": "ARRAKIS SPICE (DUNE)",
        "colors": [[255, 100, 0], [255, 150, 50], [180, 30, 0]], 
        "bg": (15, 6, 0),
        "reticle": (255, 150, 50)
    }
}

# --- Shared Engine Physics State ---
current_theme_key = "stark"
engine_state = {
    "speed_multiplier": 1.1,
    "gravity_intensity": 7.5,
    "friction": 0.90, 
    "colors": THEMES[current_theme_key]["colors"]
}

class NeuralBackground:
    """Procedural geometric web."""
    def __init__(self, node_count):
        self.nodes = []
        for _ in range(node_count):
            x = random.uniform(0, WIDTH)
            y = random.uniform(0, HEIGHT)
            vx = random.uniform(-0.15, 0.15)
            vy = random.uniform(-0.15, 0.15)
            self.nodes.append([pygame.math.Vector2(x, y), pygame.math.Vector2(vx, vy)])

    def draw_and_update(self, surface, theme_color):
        line_color = (theme_color[0], theme_color[1], theme_color[2], 25)
        for i, node in enumerate(self.nodes):
            node[0] += node[1]
            node[0].x %= WIDTH
            node[0].y %= HEIGHT
            for j in range(i + 1, len(self.nodes)):
                other_node = self.nodes[j]
                dist = node[0].distance_to(other_node[0])
                if dist < 130: 
                    pygame.draw.line(surface, line_color, (int(node[0].x), int(node[0].y)), (int(other_node[0].x), int(other_node[0].y)), 1)

def create_glow_texture(radius, color):
    """Pre-renders an ultra-smooth alpha-blended plasma cell."""
    surface = pygame.Surface((radius * 6, radius * 6), pygame.SRCALPHA)
    center = radius * 3
    for r in range(radius * 3, radius, -1):
        alpha = int(110 * (1.0 - (r / (radius * 3))) ** 2) 
        pygame.draw.circle(surface, (color[0], color[1], color[2], alpha), (center, center), r)
    for r in range(radius, 0, -1):
        alpha = int(180 + 75 * (1.0 - (r / radius)))
        pygame.draw.circle(surface, (color[0], color[1], color[2], alpha), (center, center), r)
    return surface

class HolographicNode:
    def __init__(self):
        self.pos = pygame.math.Vector2(random.uniform(0, WIDTH), random.uniform(0, HEIGHT))
        self.vel = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = random.uniform(4.0, 7.5) 
        
        self.orbit_distance = abs(random.gauss(15, 25)) 
        
        self.ring_group = random.randint(1, 3) 
        self.z_phase = random.uniform(0, math.pi * 2) 
        self.spin_direction = random.choice([-1, 1])
        self.mass = random.uniform(0.8, 2.5)
        
        self.base_color = random.choice(engine_state["colors"])
        self.texture = create_glow_texture(int(self.radius), self.base_color)

    def refresh_texture(self):
        self.base_color = random.choice(engine_state["colors"])
        self.texture = create_glow_texture(int(self.radius), self.base_color)

    def trigger_nova(self):
        """Chaotic Shatter Burst (Spacebar)"""
        center = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)
        direction = self.pos - center
        if direction.length() > 0:
            direction.normalize_ip()
            chaos_angle = random.uniform(-0.6, 0.6)
            dir_x = direction.x * math.cos(chaos_angle) - direction.y * math.sin(chaos_angle)
            dir_y = direction.x * math.sin(chaos_angle) + direction.y * math.cos(chaos_angle)
            chaotic_dir = pygame.math.Vector2(dir_x, dir_y)
            self.vel += chaotic_dir * random.uniform(140, 260) 
            
    def trigger_solar_wind(self):
        """Massive horizontal force (W)"""
        self.vel.x += random.uniform(100, 220)

    def update(self, target_x, target_y, is_tornado, time_factor):
        target = pygame.math.Vector2(target_x, target_y)
        direction = target - self.pos
        distance = direction.length()

        # To prevent massive jitter at the absolute center, we use the distance check logic
        if distance > 15:
            direction.normalize_ip() 
            
            if is_tornado:
                # L-CLICK: SHANG-CHI ENERGY RINGS (Strictly Untouched!)
                target_dist = 150 
                dist_error = distance - target_dist
                
                spring_force = direction * (dist_error * 0.08)
                self.vel += spring_force * time_factor

                tangent = pygame.math.Vector2(-direction.y, direction.x)
                if self.ring_group == 1:
                    tangent.x *= 0.15 
                    tangent.y *= 2.0
                elif self.ring_group == 2:
                    tangent.x *= 2.0  
                    tangent.y *= 0.15
                else:
                    t_rot = tangent.rotate(45)
                    t_rot.x *= 2.0
                    t_rot.y *= 0.15
                    tangent = t_rot.rotate(-45)

                self.vel += tangent * (3.0 * self.spin_direction) * time_factor

            else:
                # IDLE: PURE GRAVITY LOGIC EXTRACTED EXACTLY FROM 2ND CODE
                pull = (engine_state["gravity_intensity"] * self.mass) / (distance * 0.05)
                self.vel += direction * pull * engine_state["speed_multiplier"] * time_factor

        # Fluid wave turbulence fields
        self.vel.x += math.sin(self.pos.y * 0.012 + pygame.time.get_ticks() * 0.001) * 0.18
        self.vel.y += math.cos(self.pos.x * 0.012 + pygame.time.get_ticks() * 0.001) * 0.18

        self.vel *= engine_state["friction"]
        self.pos += self.vel * time_factor

        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT

    def draw(self, target_surface):
        offset_x = self.pos.x - (self.radius * 3)
        offset_y = self.pos.y - (self.radius * 3)
        target_surface.blit(self.texture, (int(offset_x), int(offset_y)))

def draw_hud(surface, font, theme_key):
    """Draws a crisp control dashboard overlay."""
    theme = THEMES[theme_key]
    reticle_color = theme["reticle"]
    
    texts = [
        f"SYS.STATE: {theme['name']}",
        "---------------------------------",
        "[1] Ten Rings / Stark",
        "[2] Spider-Verse (Earth-1610)",
        "[3] Interstellar (Gargantua)",
        "[4] Oppenheimer (Trinity Core)",
        "[5] Avatar (Pandora Biolume)",
        "[6] The Matrix (Digital Rain)",
        "[7] Tron Legacy (The Grid)",
        "[8] Dune (Arrakis Spice)",
        "---------------------------------",
        "[L-CLICK] Interlocking Energy Rings",
        "[SPACE]   Chaotic Nova Shatter",
        "[W]       Solar Wind Wave",
        "[R-CLICK] Time Dilation"
    ]
    
    for i, text in enumerate(texts):
        shadow = font.render(text, True, (0, 0, 0))
        surface.blit(shadow, (21, 21 + (i * 22)))
        label = font.render(text, True, reticle_color)
        surface.blit(label, (20, 20 + (i * 22)))

def ai_orchestration_worker(prompt):
    print(f"\n[AI Core] Processing contextual mutation for: '{prompt}'...")
    response_data = get_physics_parameters(prompt)
    if response_data and "colors" in response_data:
        print(f"[AI Core] AI Matrix Override Successful.")
        engine_state.update(response_data)

def check_terminal_input():
    while True:
        user_command = input("")
        if user_command.strip():
            threading.Thread(target=ai_orchestration_worker, args=(user_command,), daemon=True).start()

def main():
    pygame.init()
    pygame.font.init()
    try:
        ui_font = pygame.font.SysFont("consolas", 14, bold=True)
    except:
        ui_font = pygame.font.Font(None, 24)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("FlowState: Cinematic AI Matrix")
    clock = pygame.time.Clock()

    nodes = [HolographicNode() for _ in range(PARTICLE_COUNT)]
    bg_mesh = NeuralBackground(60) 
    
    attractor_x, attractor_y = WIDTH // 2, HEIGHT // 2
    is_tornado = False
    time_factor = 1.0 
    global current_theme_key
    
    # Smooth Cursor Variable
    smooth_x, smooth_y = float(attractor_x), float(attractor_y)
    
    threading.Thread(target=check_terminal_input, daemon=True).start()
    last_colors = list(engine_state["colors"])
    running = True

    while running:
        current_bg = THEMES[current_theme_key]["bg"]
        
        # 1. Motion Blur Layer
        trail_cover = pygame.Surface((WIDTH, HEIGHT))
        trail_cover.set_alpha(32) 
        trail_cover.fill(current_bg) 
        screen.blit(trail_cover, (0, 0))

        # 2. Procedural Background Mesh (Draws UNDER the particles)
        mesh_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        bg_mesh.draw_and_update(mesh_surface, THEMES[current_theme_key]["reticle"])
        screen.blit(mesh_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                attractor_x, attractor_y = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: is_tornado = True
                elif event.button == 3: time_factor = 0.05
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: is_tornado = False
                elif event.button == 3: time_factor = 1.0 
            elif event.type == pygame.KEYDOWN:
                theme_mapping = {
                    pygame.K_1: "stark",
                    pygame.K_2: "spiderverse",
                    pygame.K_3: "interstellar",
                    pygame.K_4: "oppenheimer",
                    pygame.K_5: "avatar",
                    pygame.K_6: "matrix",
                    pygame.K_7: "tron",
                    pygame.K_8: "dune"
                }
                if event.key in theme_mapping:
                    current_theme_key = theme_mapping[event.key]
                    engine_state["colors"] = THEMES[current_theme_key]["colors"]
                elif event.key == pygame.K_SPACE:
                    for node in nodes:
                        node.trigger_nova()
                elif event.key == pygame.K_w:
                    for node in nodes:
                        node.trigger_solar_wind()

        if engine_state["colors"] != last_colors:
            for node in nodes:
                node.refresh_texture()
            last_colors = list(engine_state["colors"])

        # FLUID CURSOR: Makes the matrix chase your mouse beautifully
        smooth_x += (attractor_x - smooth_x) * 0.1
        smooth_y += (attractor_y - smooth_y) * 0.1

        # 3. Draw the Main Particles
        for node in nodes:
            node.update(smooth_x, smooth_y, is_tornado, time_factor)
            node.draw(screen)

        # Draw a subtle core at the center of the cursor
        core_color = THEMES[current_theme_key]["reticle"]
        pygame.draw.circle(screen, core_color, (int(smooth_x), int(smooth_y)), 3)
        pygame.draw.circle(screen, (255, 255, 255), (int(smooth_x), int(smooth_y)), 1)

        # 4. Draw the UI HUD on top
        draw_hud(screen, ui_font, current_theme_key)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()