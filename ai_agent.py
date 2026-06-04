import os
import json
import random
from dotenv import load_dotenv


try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

load_dotenv()

def get_physics_parameters(user_prompt):
    """
    Attempts to use the live Gemini API. 
    If the API key is missing, internet is down, or libraries are missing,
    it seamlessly falls back to the simulated local engine to prevent crashing.
    """
    
    # --- ATTEMPT 1: LIVE GEMINI API ---
    if HAS_GENAI and os.environ.get("GEMINI_API_KEY"):
        try:
            client = genai.Client()
            system_instruction = """
            You are an advanced graphics orchestrator. Analyze the user's prompt and output a raw JSON object.
            Do not wrap the response in markdown code blocks.
            
            Choose or generate a highly cohesive, luminous 3-color palette that matches the prompt's emotion.
            
            Format your response EXACTLY like this JSON structure:
            {
                "gravity_intensity": (float between 2.0 and 18.0),
                "speed_multiplier": (float between 0.4 and 2.5),
                "friction": (float between 0.90 and 0.98, where lower means more fluid resistance),
                "colors": [
                    [R, G, B],  # Primary core color (highly intense)
                    [R, G, B],  # Secondary mid-tone color
                    [R, G, B]   # Ambient/Trail accent color
                ]
            }
            """
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    response_mime_type="application/json",
                )
            )
            print("[AI Core] Live API Connection Successful.")
            return json.loads(response.text)
            
        except Exception as e:
            print(f"[AI Core Warning] Live API failed ({e}). Booting Offline Fallback Engine...")
    else:
        print("[AI Core Warning] API Key or GenAI library missing. Booting Offline Fallback Engine...")

    # --- ATTEMPT 2: LOCAL FALLBACK SIMULATION ---
    return local_fallback_agent(user_prompt)


def local_fallback_agent(prompt):
    """Parses keywords to simulate an AI physics response entirely offline."""
    prompt = prompt.lower()
    
    # 1. Fire / Heat / Aggressive
    if any(word in prompt for word in ["fire", "lava", "red", "burn", "inferno", "heat", "sun", "flame"]):
        return {
            "colors": [[255, 30, 0], [255, 100, 0], [200, 10, 0]],
            "speed_multiplier": 1.6,   
            "friction": 0.94,          
            "gravity_intensity": 8.5
        }
        
    # 2. Water / Ice / Calm
    elif any(word in prompt for word in ["water", "ocean", "blue", "ice", "frost", "cold", "calm", "freeze"]):
        return {
            "colors": [[0, 150, 255], [0, 255, 255], [0, 50, 200]],
            "speed_multiplier": 0.7,   
            "friction": 0.85,          
            "gravity_intensity": 5.0
        }
        
    # 3. Cyberpunk / Hacker / Toxic
    elif any(word in prompt for word in ["cyber", "neon", "hack", "green", "acid", "toxic", "matrix", "tech"]):
        return {
            "colors": [[57, 255, 20], [176, 38, 255], [0, 255, 255]],
            "speed_multiplier": 1.3,
            "friction": 0.90,
            "gravity_intensity": 7.5
        }
        
    # 4. Void / Dark / Gravity
    elif any(word in prompt for word in ["dark", "void", "black hole", "gravity", "crush", "heavy", "purple"]):
        return {
            "colors": [[40, 0, 80], [20, 0, 40], [100, 0, 255]],
            "speed_multiplier": 0.9,
            "friction": 0.98,          
            "gravity_intensity": 15.0  
        }

    # 5. Generic / Unrecognized (Procedural Chaos)
    else:
        print("[AI Core] Pattern unrecognized. Initiating Procedural Chaos state...")
        return {
            "colors": [
                [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)],
                [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)],
                [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)]
            ],
            "speed_multiplier": round(random.uniform(0.8, 1.5), 2),
            "friction": round(random.uniform(0.88, 0.95), 2),
            "gravity_intensity": round(random.uniform(5.0, 9.0), 2)
        }