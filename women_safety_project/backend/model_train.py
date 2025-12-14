import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("data/crime_data.csv")

# Step 1: Feature Engineering
df["crime_severity"] = df["severity"]
df["lat"] = df["latitude"]
df["lng"] = df["longitude"]

X = df[["lat", "lng", "crime_severity"]]

# Step 2: Auto-classify Risk Levels using Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df["risk"] = kmeans.fit_predict(X)

# Step 3: Train/Test Split for ML classifier
X_train, X_test, y_train, y_test = train_test_split(
    X, df["risk"], test_size=0.2, random_state=42
)

# Step 4: Random Forest Classifier
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# Step 5: Save the trained model
joblib.dump(model, "models/model.pkl")

print("Model trained successfully!")
print("Saved at: models/model.pkl")
