# Housing Price Prediction - Comparing Different Regression Models

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Loading the housing data
file_path = r"C:\Users\Aditya Bhuran\OneDrive - Pace University\Desktop\Python-CS-661\Quiz-2\Housing.csv"
df = pd.read_csv(file_path)

print("Dataset Info:")
print(f"Total rows and columns: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nColumn types:")
print(df.dtypes)
print(f"\nAny missing data:")
print(df.isnull().sum())

# Converting text columns to numbers so model can understand
categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                       'airconditioning', 'prefarea', 'furnishingstatus']

# yes/no columns converted to 1/0
for col in categorical_columns[:-1]:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# furnishingstatus has 3 categories so using one-hot encoding
df = pd.get_dummies(df, columns=['furnishingstatus'], drop_first=True)

print("\n" + "="*80)
print("After data preprocessing:")
print(df.head())

# Separating input features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Splitting data - 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining data: {X_train.shape[0]} houses")
print(f"Testing data: {X_test.shape[0]} houses")

results = []

print("\n" + "="*80)
print("TRAINING THE MODELS")
print("="*80)

# Model 1: Simple Linear Regression (only using area)
print("\n1. Linear Regression - Using only area feature")
print("-" * 80)

lr_model = LinearRegression()
lr_model.fit(X_train[['area']], y_train)
lr_pred = lr_model.predict(X_test[['area']])

lr_mse = mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

print(f"MSE: {lr_mse:,.2f}")
print(f"R² Score: {lr_r2:.4f}")

results.append({
    'Model': 'Linear Regression',
    'MSE': lr_mse,
    'R²': lr_r2
})

# Model 2: Multiple Linear Regression (using all features)
print("\n2. Multiple Regression - Using all available features")
print("-" * 80)

mlr_model = LinearRegression()
mlr_model.fit(X_train, y_train)
mlr_pred = mlr_model.predict(X_test)

mlr_mse = mean_squared_error(y_test, mlr_pred)
mlr_r2 = r2_score(y_test, mlr_pred)

print(f"MSE: {mlr_mse:,.2f}")
print(f"R² Score: {mlr_r2:.4f}")
print(f"Total features: {X_train.shape[1]}")

results.append({
    'Model': 'Multiple Regression',
    'MSE': mlr_mse,
    'R²': mlr_r2
})

# Model 3: Polynomial Regression (degree 2)
print("\n3. Polynomial Regression - Degree 2")
print("-" * 80)

# Creating polynomial features (squares and interactions)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Scaling the features
scaler = StandardScaler()
X_train_poly_scaled = scaler.fit_transform(X_train_poly)
X_test_poly_scaled = scaler.transform(X_test_poly)

poly_model = LinearRegression()
poly_model.fit(X_train_poly_scaled, y_train)
poly_pred = poly_model.predict(X_test_poly_scaled)

poly_mse = mean_squared_error(y_test, poly_pred)
poly_r2 = r2_score(y_test, poly_pred)

print(f"MSE: {poly_mse:,.2f}")
print(f"R² Score: {poly_r2:.4f}")
print(f"Total polynomial features: {X_train_poly.shape[1]}")

results.append({
    'Model': 'Polynomial Regression (deg=2)',
    'MSE': poly_mse,
    'R²': poly_r2
})

# Comparing all models
print("\n" + "="*80)
print("RESULTS COMPARISON")
print("="*80)

results_df = pd.DataFrame(results)
print("\n" + results_df.to_string(index=False))

best_r2_model = results_df.loc[results_df['R²'].idxmax(), 'Model']
best_mse_model = results_df.loc[results_df['MSE'].idxmin(), 'Model']

print("\n" + "="*80)
print("="*80)
print(f"\nHighest R² score: {best_r2_model} with {results_df['R²'].max():.4f}")
print(f"Lowest MSE: {best_mse_model} with {results_df['MSE'].min():,.2f}")
print("="*80)
