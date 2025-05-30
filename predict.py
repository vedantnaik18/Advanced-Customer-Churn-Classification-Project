import joblib
import pandas as pd

# Load the trained model
model = joblib.load('XGB_Churn_model.pkl')

# Define the prediction function
def predict_churn(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    return {"prediction": int(prediction), "churn_probability": round(probability, 2)}
