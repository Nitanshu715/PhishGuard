# train_model.py (ADVANCED + AUTO CLEANING)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
import os
print("Loading dataset...")
df = pd.read_csv("../urlset.csv", on_bad_lines="skip", encoding="latin-1", low_memory=False)
print("Cleaning data...")
# Convert all columns except domain + label to numeric
for col in df.columns:
    if col not in ["domain", "label"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
# Remove rows where label is missing
df = df.dropna(subset=["label"])
# Fill missing numeric values with 0 (safe choice for ML)
df = df.fillna(0)
# Split X and y
y = df["label"]
X = df.drop(columns=["label", "domain"], errors="ignore")
print("Final feature count:", X.shape[1])
# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Training model...")
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)
acc = model.score(X_test, y_test)
print(f"Accuracy: {acc * 100:.2f}%")
# Save model to backend
output_path = "../backend/model.pkl"
dump(model, output_path)
print("Model saved ->", output_path)
