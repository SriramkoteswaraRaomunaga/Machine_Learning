import json
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

def train_and_evaluate():
    print("Loading skills dataset...")
    # Load dataset
    df = pd.read_csv(os.path.join("data", "skills_dataset.csv"))
    
    # Define features and target
    X = df.drop(columns=["Role"])
    y = df["Role"]
    
    skills_list = list(X.columns)
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    
    # Train Random Forest Classifier
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)
    
    # Evaluate model
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    
    report = classification_report(y_test, y_pred, output_dict=True)
    conf_mat = confusion_matrix(y_test, y_pred, labels=model.classes_)
    
    # Calculate feature importances
    importances = model.feature_importances_
    feature_importance_df = pd.DataFrame({
        "Skill": skills_list,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False)
    
    feature_importance_list = feature_importance_df.to_dict(orient="records")
    
    # Save directory
    os.makedirs("models", exist_ok=True)
    
    # Save the model
    model_path = os.path.join("models", "model.joblib")
    joblib.dump(model, model_path)
    print(f"Model saved successfully to: {model_path}")
    
    # Prepare metadata to save
    metadata = {
        "accuracy": accuracy,
        "classes": list(model.classes_),
        "skills": skills_list,
        "feature_importance": feature_importance_list,
        "confusion_matrix": conf_mat.tolist(),
        "classification_report": report
    }
    
    metadata_path = os.path.join("models", "model_metadata.json")
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)
        
    print(f"Metadata saved successfully to: {metadata_path}")

if __name__ == "__main__":
    train_and_evaluate()
