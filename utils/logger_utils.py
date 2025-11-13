import os
from datetime import datetime

LOG_DIR = os.path.join("cloudconnect", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

def now_ts():
    return datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

def write_log(resource_name, message):
    path = os.path.join(LOG_DIR, f"{resource_name}.log")
    with open(path, "a", encoding="utf-8") as f:
        f.write(message + "\n")