# 🌌 FlowState: 3D Orbital Plasma Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![Google Gemini](https://img.shields.io/badge/AI-Gemini_2.5_Flash-orange?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)

> **A high-fidelity, 60-FPS 3D particle orchestration engine demonstrating advanced interactive orbital mechanics, mathematical clustering, and cinematic fluid physics.**



---

## 🚀 Overview

**FlowState** bridges interactive computational geometry with cinematic rendering pipelines. Built entirely from scratch on top of Pygame’s low-level surface manipulation, the engine manages **900 independent structural nodes** smoothly at maximum refresh rates. It explores how mathematical formulas (like Gaussian distributions and Vector3 matrix rotations) can be used to simulate organic, visually stunning energy fields.

---

## 🧠 Technical Architecture & Optimizations

This engine achieves its high performance and visual fidelity through several core computer science optimizations:

* **Strict Gravitational Vector Mechanics:** Node vectors interact dynamically with a real-time fluid cursor attractor. Instead of fixed coordinate positioning, particles use pure mass-to-distance acceleration logic to calculate dynamic velocity vectors.
* **Gaussian Core Distribution:** To prevent central computational hollowing (the "donut hole" effect), the core idle state utilizes a specialized Gaussian Distribution curve (`random.gauss`) to tightly cluster 85% of particles into an opaque, white-hot core that naturally feathers outward.
* **Vector3 Matrix Rotations:** When interactive states change, the matrix dynamically calculates true 3D spatial geometry using sequential rotation operations on the X, Y, and Z axes to generate perfect interlocking, collision-free energy bands.
* **Scalable Alpha-Blended Texture Caching:** To minimize pixel-drawing overhead, a pre-rendered radial glow asset cache scales graphics dynamically based on real-time Z-depth coordinates, decoupling visual fidelity from processing bottlenecks.
* **Zero-Downtime Hybrid AI Orchestration:** The engine incorporates an isolated background thread handler to process incoming context modifications concurrently via the **Google Gemini API**. If the API is unreachable (no internet or missing keys), it seamlessly shifts to a localized, offline procedural fallback engine to guarantee 100% uptime.

---

## 🎮 Interactive Controls

Run the engine and use the following interface keys to manipulate the plasma matrix in real-time:

| Input | Action | Description |
| :--- | :--- | :--- |
| **Mouse Move** | Fluid Tracking | Smooth cursor tracking via Linear Interpolation (LERP). |
| **Left-Click (Hold)**| Orbital Rings | Toggles true 3D interlocking orbital energy rings. |
| **Spacebar** | Nova Shatter | Triggers a catastrophic explosive shockwave from the core. |
| **W Key** | Solar Wind | Launches a directional cosmic wave sweeping across the canvas. |
| **Right-Click (Hold)**| Time Dilation | Initiates a 0.05x speed slow-motion effect. |
| **Terminal Input** | AI Override | Type natural language (e.g., *"Make it look like cyberpunk fire"*) in the terminal to dynamically alter physics and colors. |

---

## 🎨 Cinematic Color Profiles

Press keys `1` through `8` to instantly swap between meticulously crafted, cinema-inspired color grading profiles:

1. **Stark Industries** *(Deep Reds & Gold)*
2. **Spider-Verse (Earth-1610)** *(Vibrant Neons & Magentas)*
3. **Gargantua Accretion Disk** *(Intense Oranges & Blues)*
4. **Trinity Core** *(Blistering Atomic Whites & Reds)*
5. **Pandora Bioluminescence** *(Bioluminescent Cyan & Purple)*
6. **The Matrix** *(Digital Rain Greens)*
7. **Tron Legacy** *(Grid Cyans & Pinks)*
8. **Arrakis Spice** *(Desert Oranges & Ambers)*

---

## 🛠️ Installation & Execution

FlowState is designed to be lightweight and frictionless. 

**1. Clone the repository:**
```bash
git clone (https://github.com/VinayakMehta007/FlowState-3D-Orbital-Plasma-Engine.git)
cd FlowState-3D-Orbital-Plasma-Engine
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set up the Live AI Orchestrator (Optional) To enable the live Google Gemini 2.5 physics mutations, you need to provide an API key:**

* Duplicate the included .env.example file.
* Rename the duplicated file to .env.
* Open it and paste your API key inside.

💡 Bulletproof Fallback Architecture: If you skip this step, lose internet connection, or lack the GenAI libraries, the engine will not crash. It is engineered to seamlessly detect the missing credentials and default to an embedded Local Procedural AI Agent to guarantee 100% uptime.

**4. Ignite the Engine**
```bash
python main.py
```

---

## 🛡️ License & Acknowledgements

This engine was architected for showcase and educational purposes to explore interactive computational physics, organic clustering mathematics, and Python hardware rendering limits.

Feel free to fork the repository, dive into the code, and modify the physics constants to create your own cinematic orbital themes!

### **Author & Architect: Vinayak Mehta**
