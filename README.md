# DevOps + MLOps Pipeline Implementation

## 📌 Project Overview

This project demonstrates an end-to-end DevOps and MLOps pipeline using:

- GitHub for version control
- GitHub Actions for CI/CD
- DVC for dataset versioning
- MLflow for experiment tracking
- Docker for containerization
- Email alerts for failure handling

---

## 🏗 Project Structure

.
├── src/
│ ├── app.py
│ ├── train.py
├── data/
│ ├── dataset.csv.dvc
├── .github/workflows/
│ ├── ci.yml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md


---

## ⚙️ Setup Instructions (Local Execution)

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Training Script
python src/train.py
4️⃣ Launch MLflow UI
mlflow ui
Open browser:

http://127.0.0.1:5000
📦 Dataset Versioning (DVC)
Initialize DVC:

dvc init
Track dataset:

dvc add data/dataset.csv
Push data to DVC remote:

dvc push
🔬 Experiment Tracking (MLflow)
Experiment Name: devops-mlops-lab

Metric Logged: Mean Squared Error (MSE)

🚀 CI/CD Pipeline
On every push:

Install dependencies

Run Python script

Execute training

Verify pipeline execution

🐳 Docker Execution (If Docker Installed)
Build image:

docker build -t devops-mlops-lab .
Run container:

docker run devops-mlops-lab
🛠 Tools & Technologies Used
Python

Git

GitHub

GitHub Actions

DVC

MLflow

Docker

scikit-learn

pandas

✅ Deliverables
Public GitHub repository

DVC tracked dataset

MLflow experiment with logged metric

CI/CD workflow

Docker configuration

Email alert integration

