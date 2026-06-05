import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

np.random.seed(42)

n_matches = 1000

home_form = np.random.uniform(40, 85, n_matches)
away_form = np.random.uniform(40, 85, n_matches)
home_toss = np.random.randint(0, 2, n_matches)
is_day_match = np.random.randint(0, 2, n_matches)
home_rest = np.random.randint(2, 7, n_matches)
away_rest = np.random.randint(2, 7, n_matches)

match_score = (
    (home_form - away_form)
    + (home_toss * 5)
    + (home_rest - away_rest)
)

home_wins = (match_score > 0).astype(int)

df = pd.DataFrame({
    "home_team_form": home_form,
    "away_team_form": away_form,
    "home_won_toss": home_toss,
    "day_match": is_day_match,
    "home_rest_days": home_rest,
    "away_rest_days": away_rest,
    "home_win": home_wins
})

X = df.drop("home_win", axis=1)
y = df["home_win"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully")
