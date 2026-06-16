# AI-Powered Career Role Prediction & Skill Gap Analysis System

An intelligent, data-driven system built using **Python, Scikit-learn, Pandas, Streamlit, and Plotly** to predict suitable career roles, analyze skill gaps, and generate personalized learning roadmaps.

---

## 🚀 Key Features

- **Multi-Category Skill Selection**: Select skills dynamically across Programming, Data Visualization, Databases, Machine Learning, Deep Learning, NLP, Cloud, and Soft Skills.
- **Top-3 Role Recommendations**: Uses a trained machine learning classifier to return the top 3 matching career roles along with confidence scores.
- **Career Readiness Score**: Real-time gauge chart displaying percentage match for the recommended role.
- **Side-by-Side Skill Gap Visualization**: Interactive Plotly bar chart comparing candidates' skills directly with average industry requirements.
- **Personalized Learning Roadmaps**: Actionable steps, duration estimates, books, online courses, and hands-on projects to bridge missing skills.
- **Interactive ML Diagnostics Tab**: Inspect overall test accuracy (92.25%), confusion matrix heatmap, class performance details, and feature importances.

---

## 🛠️ Architecture & System Structure

```
project/
├── data/
│   ├── generate_data.py          # Script to generate realistic synthetic dataset
│   └── skills_dataset.csv        # Generated CSV file containing skills and labels
├── models/
│   ├── train.py                  # Script to preprocess data, train Random Forest, evaluate and save model
│   ├── model.joblib              # Serialized trained Scikit-learn model
│   └── model_metadata.json       # Stores features list, label classes, and evaluation metrics
├── app/
│   ├── main.py                   # Streamlit main entrypoint
│   ├── styles.py                 # Custom CSS stylesheet rules and page configurations
│   └── roadmap_data.py           # Personalized roadmap resources and course suggestions per skill
├── requirements.txt              # Project dependencies
└── README.md                     # This documentation
```

### Supported Roles
1. **Data Scientist**
2. **Machine Learning Engineer**
3. **Data Analyst**
4. **Software Engineer (Full-Stack)**
5. **Cloud Architect / DevOps**
6. **Database Administrator (DBA)**
7. **NLP Engineer**
8. **Product Manager**

---

## ⚙️ Setup & Installation

### 1. Install Dependencies
Ensure you have Python 3.8+ installed. Install project requirements using:
```bash
pip install -r requirements.txt
```

### 2. Generate Synthetic Dataset
Generate the synthetic dataset (2,000 samples) by running:
```bash
python data/generate_data.py
```

### 3. Train the Model
Preprocess the dataset and train the Random Forest Classifier by running:
```bash
python models/train.py
```
This trains the model, outputs evaluation metrics, and saves the trained classifier (`model.joblib`) and metadata (`model_metadata.json`).

### 4. Run the Streamlit Dashboard
Launch the web application locally:
```bash
streamlit run app/main.py
```
Open the URL shown in the terminal (typically `http://localhost:8501`) to experience the interactive dashboard.

---

## 📊 Model Details

- **Algorithm**: Random Forest Classifier
- **Features**: 40 distinct technical and soft skills (binary 0/1 inputs)
- **Target**: 8 professional roles
- **Performance**: Test accuracy of **92.25%** with stratified test validation
- **Metrics Tracked**: Precision, Recall, F1-Score, and Confusion Matrix
