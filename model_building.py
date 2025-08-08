# model_building.py

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib

from preprocess_data import create_features  # Reuse your function

processed_folder = "processed"
output_folder = "predictions"
os.makedirs(output_folder, exist_ok=True)

# Define targets and features
target_columns = ['Target_1d', 'Target_7d', 'Target_30d', 'Target_365d']
feature_columns = ['Return', 'Volatility', 'Momentum']

results = {}

# Iterate through all CSVs in processed folder
for file_name in os.listdir(processed_folder):
    if not file_name.endswith(".csv"):
        continue

    print(f"\nProcessing {file_name}...")

    df = pd.read_csv(os.path.join(processed_folder, file_name))
    df = create_features(df)

    asset_results = {}

    for target in target_columns:
        # Prepare features and labels
        X = df[feature_columns]
        y = df[target]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

        asset_results[target] = {
            "mse": mse,
            "last_prediction": y_pred[-1]
        }

        # Save model
        model_path = f"models/{file_name.replace('.csv','')}_{target}.pkl"
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, model_path)

        # Save predictions
        pred_df = pd.DataFrame({
            "Actual": y_test.values,
            "Predicted": y_pred
        })
        pred_df.to_csv(f"{output_folder}/{file_name.replace('.csv','')}_{target}.csv", index=False)

    results[file_name.replace(".csv", "")] = asset_results

# Final summary
print("\n=== Model Training Complete ===")
for asset, asset_results in results.items():
    print(f"\n📊 {asset}")
    for target, metrics in asset_results.items():
        print(f"  ➤ {target}: MSE = {metrics['mse']:.4f}, Last Prediction = {metrics['last_prediction']:.2f}")
