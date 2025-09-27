import requests

url = "http://127.0.0.1:5000/predict"

# Replace this with realistic values from your diabetes dataset
data = {
    "features": {
        "Pregnancies": 2,
        "Glucose": 130,
        "BloodPressure": 70,
        "SkinThickness": 25,
        "Insulin": 80,
        "BMI": 28.1,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 32
    }
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
