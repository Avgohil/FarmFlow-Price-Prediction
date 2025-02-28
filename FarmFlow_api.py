from fastapi import FastAPI
import joblib
import pandas as pd

# API app initialize
app = FastAPI()

# Model & Encoder Load karo
model = joblib.load("FarmFlow_Price_Model.pkl")
encoder = joblib.load("commodity_label_encoder.pkl")

# Prediction Function
def predict_price(year: int, month: int, day: int, commodity_name: str):
    if commodity_name not in encoder.classes_:
        return {"error": "Invalid commodity name"}
    
    commodity_encoded = encoder.transform([commodity_name])[0]
    input_data = pd.DataFrame([[year, month, day, commodity_encoded]], columns=["year", "month", "day", "commodity_encoded"])
    predicted_price = model.predict(input_data)[0]
    
    return {
        "date": f"{year}-{month:02d}-{day:02d}",
        "commodity": commodity_name,
        "predicted_price": round(predicted_price, 2)
    }

# API Route
@app.get("/predict/")
def get_prediction(year: int, month: int, day: int, commodity_name: str):
    return predict_price(year, month, day, commodity_name)
