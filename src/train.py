import os
import traceback
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow

from email_alerts import send_failure_email

DATA_PATH = "data/dataset.csv"
TARGET_COL = "label"


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
    try:
        main()

    except Exception:
        err = traceback.format_exc()
        print("❌ Training failed.")
        print(err)

        # Send email only if EMAIL_USER exists (local environment)
        if os.getenv("EMAIL_USER"):
            try:
                send_failure_email(
                    subject="DevOps-MLOps Lab: Training Failed",
                    body=f"Training pipeline failed.\n\nError:\n{err}",
                )
                print("✅ Failure email sent.")
            except Exception as mail_err:
                print("⚠️ Email sending failed:", mail_err)
        else:
            print("⚠️ Email not configured (CI environment). Skipping email.")

        raise
