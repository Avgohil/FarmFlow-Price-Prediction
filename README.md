
# FarmFlow Price Prediction AI

## Overview
FarmFlow's Price Prediction AI leverages machine learning to forecast the prices of agricultural products based on historical data, market trends, and various influencing factors. This tool helps farmers and buyers make informed decisions about pricing and trade.

## Features
- **AI-driven Price Prediction**: Uses machine learning algorithms to forecast product prices.
- **FastAPI Integration**: Provides a lightweight and efficient API for predictions.
- **Historical Data Analysis**: Utilizes past market trends to improve prediction accuracy.
- **Scalable & Efficient**: Can be extended to incorporate more data and advanced models.

## Tech Stack
- **Backend**: Python, FastAPI
- **Machine Learning**: Scikit-learn, Pandas, NumPy

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- FastAPI
- Uvicorn
- Scikit-learn, Pandas, NumPy

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/farmflow-price-prediction.git
   cd farmflow-price-prediction
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the FastAPI application:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Usage
1. Upload historical price data.
2. Select the prediction model.
3. Use the FastAPI endpoint to get AI-driven price forecasts.
4. Utilize insights for better market decisions.

### API Endpoints
- **`POST /predict`** - Send input features and get price prediction.
- **`GET /docs`** - Access the FastAPI Swagger UI for API testing.

## Dataset
Download realtime data from # https://ceda.ashoka.edu.in/data-portal/#
The model is trained using a dataset that includes:
- Product name
- Market price history
- Seasonal trends
- Supply and demand factors

## AI Model
- Utilizes **Linear Regression** and **Random Forest** for price prediction.
- Feature engineering to improve prediction accuracy.
- Hyperparameter tuning for better results.


## Project Team
- **AI & Machine Learning Implementation**: Handled by [Ankita gohil(Me)]


