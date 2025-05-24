import json
import os

DB_PATH = "database.json"

def load_db():
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump({"users": {}}, f)
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def add_skin_tone(username, tone):
    db = load_db()
    user = db["users"].setdefault(username, {})
    history = user.setdefault("skin_tone_history", [])
    history.append(tone)
    save_db(db)
