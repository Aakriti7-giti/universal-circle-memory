from fastapi import FastAPI
from main import UniversalCircleMemory
import os

app = FastAPI(title="Universal Circle Memory - Production Ready")
brain = UniversalCircleMemory()

@app.get("/")
def home():
    return {
        "status": "LIVE",
        "message": "Universal Circle Memory is running",
        "solari_connected": brain.client is not None,
        "circle_id": os.getenv("SOLARI_CIRCLE_ID", "universal-circle-memory"),
        "endpoints": ["/add", "/recall", "/fork"]
    }

@app.post("/add")
def add_memory(person: str, content: str, gravity: float = 0.5):
    mem = brain.add_memory(content, person, gravity)
    return {"saved": True, "memory": mem, "real_solari": brain.client is not None}

@app.get("/recall")
def recall(min_gravity: float = 0.8):
    results = brain.recall_by_gravity(min_gravity)
    return {"count": len(results), "memories": results}

@app.post("/fork")
def fork(person: str, old: str, new: str):
    result = brain.fork_memory(person, old, new)
    return {"forked": True, "result": result}
