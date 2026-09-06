import os
from datetime import datetime

try:
    from solari import Solari
    REAL_SOLARI = True
except ImportError:
    REAL_SOLARI = False

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

API_KEY = os.getenv("SOLARI_API_KEY")
CIRCLE_ID = os.getenv("SOLARI_CIRCLE_ID", "universal-circle-memory")

class UniversalCircleMemory:
    def __init__(self):
        self.memories = []
        self.client = None
        
        if REAL_SOLARI and API_KEY and API_KEY != "your_api_key_here":
            try:
                self.client = Solari(api_key=API_KEY)
                self.circle = self.client.circles.get(CIRCLE_ID)
                print(f"✅ REAL Solari Connected: Circle {CIRCLE_ID}")
            except Exception as e:
                print(f"⚠️ Solari connect failed, using local demo: {e}")
                self.client = None
        else:
            print("🧪 Running in LOCAL DEMO mode (add real API key in .env to go LIVE)")
        
    def add_memory(self, content, person, gravity=0.5, tags=None):
        memory = {
            "content": content,
            "person": person,
            "gravity": gravity,
            "tags": tags or [],
            "timestamp": datetime.now().isoformat(),
            "forks": []
        }
        
        if self.client:
            try:
                self.client.memories.create(
                    circle_id=CIRCLE_ID,
                    content=content,
                    gravity=gravity,
                    metadata={"person": person, "tags": tags}
                )
                print(f"   → Saved to REAL Solari Cloud!")
            except Exception as e:
                print(f"   → Local save (cloud error: {e})")
        
        self.memories.append(memory)
        return memory
    
    def fork_memory(self, person, old_content, new_content):
        for m in self.memories:
            if m["person"] == person and old_content in m["content"]:
                m["forks"].append({"old": m["content"], "timestamp": m["timestamp"]})
                m["content"] = new_content
                print(f"   → FORK tracked: {old_content} -> {new_content}")
                return m
        return None

    def recall_by_gravity(self, min_gravity=0.8):
        results = sorted([m for m in self.memories if m["gravity"] >= min_gravity], 
                        key=lambda x: x["gravity"], reverse=True)
        if self.client:
            try:
                real_results = self.client.memories.search(circle_id=CIRCLE_ID, min_gravity=min_gravity)
                print(f"   → Recalled {len(real_results)} from REAL Solari")
                return real_results
            except:
                pass
        return results

if __name__ == "__main__":
    print("=== Universal Circle Memory - LIVE Solari Demo ===")
    brain = UniversalCircleMemory()
    brain.add_memory("Mom birthday is May 10 - BUY CAKE", "Mom", gravity=0.95, tags=["birthday", "family"])
    brain.add_memory("Rahul likes black coffee", "Rahul", gravity=0.7, tags=["like"])
    brain.add_memory("Promise: Help Aakriti with startup pitch by Friday", "Aakriti", gravity=0.9, tags=["promise", "work"])
    print("\n--- Testing FORK ---")
    brain.fork_memory("Rahul", "black coffee", "Rahul likes cold brew now")
    print("\n--- Testing GRAVITY ---")
    important = brain.recall_by_gravity(0.8)
    for mem in important:
        print(mem)
