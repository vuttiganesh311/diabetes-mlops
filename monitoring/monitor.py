import requests
import time
from datetime import datetime

API_URL = "http://127.0.0.1:5000/predict"
SLEEP_INTERVAL = 10  # seconds

def monitor():
    payload = {
        "features": {
            "Pregnancies": 2,
            "Glucose": 120,
            "BloodPressure": 70,
            "SkinThickness": 25,
            "Insulin": 100,
            "BMI": 30.0,
            "DiabetesPedigreeFunction": 0.5,
            "Age": 25
        }
    }

    print("🚀 Starting API monitor... Press Ctrl+C to stop.\n")

    while True:
        try:
            response = requests.post(API_URL, json=payload)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if response.status_code == 200:
                print(f"[{timestamp}] ✅ Response: {response.json()}")
            else:
                print(f"[{timestamp}] ⚠️ Unexpected status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] ❌ Request failed: {e}")

        time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")
