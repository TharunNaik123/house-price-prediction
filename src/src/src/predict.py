import pickle
import pandas as pd

# Load model
with open("model/linear_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example sample
sample = pd.DataFrame([{
    "rooms": 3,
    "area_sqft": 1200,
    "age": 10,
    "distance_city_center_km": 5
}])

# Prediction
prediction = model.predict(sample)[0]
print("Predicted Price (Lakhs):", prediction)
