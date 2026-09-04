import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Connected to Solari! (local universal circle)")

# === LOCAL UNIVERSAL CIRCLE MEMORY WITH FORK + GRAVITY ===
class UniversalCircle:
    def __init__(self, name):
        self.name = name
        self.memories = []
        print(f"Universal Circle Memory '{name}' Created!")

    def add(self, content, gravity=0.5):
        self.memories.append({
            "content": content,
            "gravity": gravity,
            "date": str(datetime.now()),
            "forks": []
        })
        print(f" Saved [gravity {gravity}]: {content}")

    def fork(self, old_content, new_content):
        for m in self.memories:
            if old_content in m["content"]:
                m["forks"].append({"old": old_content, "new": new_content})
                m["content"] = new_content
                print(f" Forked: '{old_content}' -> '{new_content}'")
                return
        print(" Old memory not found, adding as new")
        self.add(new_content, gravity=0.7)

    def search(self, query, top_k=2):
        # Simple search: sort by gravity + keyword match
        scored = []
        for m in self.memories:
            score = m["gravity"]
            if any(word.lower() in m["content"].lower() for word in query.split()):
                score += 0.5
            scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1]["content"] + f" [gravity={s[1]['gravity']}]" for s in scored[:top_k]]

# Create circle
circle = UniversalCircle("universal-circle")

# --- DEMO: Everyone needs this ---
circle.add("Mom: Birthday is 5th May - never forget", gravity=0.95)
circle.add("Rahul: Likes black coffee, preparing for UPSC", gravity=0.7)
circle.add("Priya: Promised to help with startup pitch on Friday", gravity=0.9)

print("\nSaved 3 memories with gravity!")

circle.fork("Rahul: Likes black coffee, preparing for UPSC", "Rahul: Likes black coffee, now also likes cold brew")
print("Forked Rahul's memory!")

print("\n--- Recall results ---")
results = circle.search("What does Rahul like?", top_k=2)
for r in results:
    print(f" -> {r}")

results2 = circle.search("promises", top_k=2)
for r in results2:
    print(f" -> {r}")

print("\n=== PROJECT DONE === Universal Circle Memory ready for all!")
