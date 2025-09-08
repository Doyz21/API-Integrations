import json
import os

def save_to_json(data, filename):
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Data was saved to: {filepath}")