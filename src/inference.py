from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_json = request.get_json()
    features = input_json["features"]
    input_df = pd.DataFrame([features])
    prediction = model.predict(input_df)[0]
    prediction_text = "Yes" if prediction == 1 else "No"
    return jsonify({"prediction": prediction_text})

if __name__ == "__main__":
    app.run(debug=True)
