import subprocess
import json
import webbrowser
import requests
import os

# Set up paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

APP_SCRIPT_PATH = os.path.join(BASE_DIR, "..", "product_generator", "app.py")
PRODUCT_JSON_PATH = os.path.join(BASE_DIR, "..", "orchestrator", "product_info.json")
MOCKUP_RELATIVE_PATH = "mockup_visualizer/index.html"

# Step 1: Run product_generator/app.py
print("🚀 Running product generator...")
product_proc = subprocess.run(["python", APP_SCRIPT_PATH])

# Step 2: Read generated product_info.json
if not os.path.exists(PRODUCT_JSON_PATH):
    raise Exception("product_info.json not found. Product generation failed.")

with open(PRODUCT_JSON_PATH, "r") as f:
    product = json.load(f)

print("\n Product Info:")
print(json.dumps(product, indent=2))

# Step 3: Send data to fake Node.js publisher
print("\n Publishing product to fake endpoint...")
try:
    response = requests.post("http://localhost:4000/publish", json=product)
    print("✅ Server Response:")
    print(response.json())
except Exception as e:
    print(" Failed to publish:", e)
    
# Step 4: Open mockup visualizer served at localhost
print("\n🌐 Opening mockup visualizer...")
# Replace with your actual port (e.g., 5500 or another you use)
PORT = 5500
webbrowser.open(f"http://localhost:{PORT}/{MOCKUP_RELATIVE_PATH}")
