from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return "IPL Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    sample = pd.DataFrame([{
        "home_team_form": data["home_team_form"],
        "away_team_form": data["away_team_form"],
        "home_won_toss": data["home_won_toss"],
        "day_match": data["day_match"],
        "home_rest_days": data["home_rest_days"],
        "away_rest_days": data["away_rest_days"]
    }])

    prediction = model.predict(sample)[0]

    if prediction == 1:
        result = "Home Team Wins"
    else:
        result = "Away Team Wins"

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)
