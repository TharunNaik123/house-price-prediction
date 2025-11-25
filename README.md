# House Price Prediction
Requirements.txt
pandas
numpy
scikit-learn
pickle-mixin

### Tasks completed 
This project predicts house prices using Linear Regression.

 1.Data Generation (Synthetic housing dataset)  
 2.Data Cleaning & Feature Selection  
 3.Train/Test Split  
 4.Model Training (Linear Regression)  
 5.RMSE & R² Evaluation  
 6.Saving the Trained Model  
 7.Example Predictions 
 
 How to Run
 ## 1. Train the model
python src/train.py
## 2. Run predictions
python src/predict.py
Model will be saved inside `/model/linear_model.pkl`.

 ### MODEL RESULTS 

RMSE: 9.75
R² Score: 0.936

Example Predictions (first 5 test samples):
[75.95, 51.58, 112.47, 97.44, 74.65]   (in Lakhs)
