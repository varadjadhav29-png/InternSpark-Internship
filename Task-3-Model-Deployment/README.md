# Task 3 - Model Deployment API & Containerization

## Project Overview

This project deploys an IPL Match Prediction Machine Learning model using Flask and Docker.

## Features Used

- Home Team Form
- Away Team Form
- Toss Result
- Day/Night Match
- Home Team Rest Days
- Away Team Rest Days

## Model

Random Forest Classifier

## API Endpoint

POST /predict

Sample Input

{
  "home_team_form": 80,
  "away_team_form": 55,
  "home_won_toss": 1,
  "day_match": 0,
  "home_rest_days": 5,
  "away_rest_days": 3
}

Sample Output

{
  "prediction": "Home Team Wins"
}

## Run Locally

python train_model.py

python app.py

## Docker

docker build -t ipl-api .

docker run -p 5000:5000 ipl-api

## Project Screenshots

**1. Server Running Locally**
![Terminal output showing server running]

**2. Web Application Interface**
![Home page of the web app]

**3. Model Prediction Output**
![Prediction result from the model]

#Author - Varad Jadhav 
