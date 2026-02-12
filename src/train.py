import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow

DATA_PATH = "data/dataset.csv"
TARGET_COL = "label"   # <-- THIS IS YOUR LABEL COLUMN

def main():
    df = pd.read_csv(DATA_PATH)

    if TARGET_COL not in df.columns:
        raise ValueError(f"Dataset must contain '{TARGET_COL}' column.")

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    mlflow.set_experiment("devops-mlops-lab")

    with mlflow.start_run():
        mlflow.log_metric("mse", mse)

    print(f"✅ Training complete. MSE={mse:.4f}")

if __name__ == "__main__":
    main()
