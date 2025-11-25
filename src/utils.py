import pandas as pd
import numpy as np

def generate_dataset(n=5000):
    np.random.seed(42)
    df = pd.DataFrame({
        "rooms": np.random.randint(1, 8, n),
        "area_sqft": np.random.randint(400, 4000, n),
        "age": np.random.randint(0, 50, n),
        "distance_city_center_km": np.random.uniform(1, 30, n)
    })

    df["price_lakhs"] = (
        df["rooms"] * 15 +
        df["area_sqft"] * 0.02 -
        df["age"] * 0.3 -
        df["distance_city_center_km"] * 0.8 +
        np.random.normal(0, 10, n)
    )

    return df
