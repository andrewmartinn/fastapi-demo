from pathlib import Path
import json

# create a data directory
DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "posts.json"

# load data from data file
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    else:
        return []

# save data to data file
def save_data(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        f.write(json.dumps(data, indent=2))