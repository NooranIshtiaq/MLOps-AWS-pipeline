#------------------------- ASSIGNMENT # 01 -------------------------
# Nooran Ishtiaq
# 22I-2010
# DS-B
# MLOPS


import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime
import os

DATA_PATH = "/mnt/ml-data/datasets/processed.csv"
MODEL_PATH = "/mnt/ml-data/models/best_model.pkl"
LOG_PATH = "/mnt/ml-data/logs/metrics.log"
FEATURE_PATH = "/mnt/ml-data/features/"

# -------------------------------------------------
# Loading Dataset

print("Loading dataset...")
data = pd.read_csv(DATA_PATH)
X = data.drop("income", axis=1)
y = data["income"]

#--------------------------------------------------
# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# -------------------------------------------------
# 3. Feature Scaling

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------------------------
# Save Features

print("Saving scaled features...")
os.makedirs(FEATURE_PATH, exist_ok=True)
pd.DataFrame(X_train).to_csv(FEATURE_PATH + "X_train_scaled.csv", index=False)
pd.DataFrame(X_test).to_csv(FEATURE_PATH + "X_test_scaled.csv", index=False)
joblib.dump(scaler, FEATURE_PATH + "scaler.pkl")
print("Features saved in:", FEATURE_PATH)

# -------------------------------------------------
# 4. Train Two Models
print("Training models...")

model1 = LogisticRegression(max_iter=1000)
model2 = RandomForestClassifier(random_state=42)
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)

# -------------------------------------------------
# 5. Evaluate Models

pred1 = model1.predict(X_test)
pred2 = model2.predict(X_test)
acc1 = accuracy_score(y_test, pred1)
acc2 = accuracy_score(y_test, pred2)

print(f"Logistic Regression Accuracy: {acc1}")
print(f"Random Forest Accuracy: {acc2}")

# -------------------------------------------------
# 6. Select Best Model
if acc1 > acc2:
    best_model = model1
    best_accuracy = acc1
    model_name = "LogisticRegression"
else:
    best_model = model2
    best_accuracy = acc2
    model_name = "RandomForest"

print(f"Best Model: {model_name}")

# -------------------------------------------------
# 7. Save Best Model

joblib.dump(best_model, MODEL_PATH)
print("Best model saved at:", MODEL_PATH)

# -------------------------------------------------
# 8. Log Metrics

with open(LOG_PATH, "a") as f:
    f.write(f"Model: {model_name}\n")
    f.write(f"Accuracy: {best_accuracy}\n")
    f.write(f"Timestamp: {datetime.now()}\n")
    f.write("-" * 30 + "\n")

print("Metrics logged at:", LOG_PATH)
print("Training pipeline completed successfully!")
