from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    input_json = request.get_json()
    features = input_json["features"]
    input_df = pd.DataFrame([features])
    prediction = model.predict(input_df)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
