# 🌍 AI-Powered Mood-Based Trip Recommendation System

## 📌 Project Overview

The AI-Powered Mood-Based Trip Recommendation System helps users discover travel destinations based on their emotional state.

The system uses Natural Language Processing (NLP) and Machine Learning to analyze user text, identify emotions, map emotions to travel moods, and recommend suitable travel destinations.

Instead of directly predicting a location, the system detects the user's emotional condition and provides personalized travel recommendations.

---

## 🚀 Features

- Emotion Detection using NLP
- Text Preprocessing
  - Lowercasing
  - Stopword Removal
  - Lemmatization
  - Regex Cleaning
- TF-IDF Feature Engineering
- Logistic Regression Classification
- Mood Mapping
- Travel Destination Recommendation
- Budget-Based Filtering
- Season-Based Filtering
- Top Rated Destination Suggestions

---

## 🏗️ Project Workflow

User Input
↓
Text Cleaning
↓
TF-IDF Vectorization
↓
Emotion Detection
↓
Mood Mapping
↓
Destination Recommendation
↓
Top Travel Suggestions

---

## 📊 Dataset

### Emotion Dataset

Contains over 100,000 text records with emotion labels.

| Column | Description |
|----------|-------------|
| sentence | User text |
| emotion | Emotion label |

Example:

| sentence | emotion |
|----------|----------|
| I am feeling very happy today | joy |
| I feel lonely and depressed | sadness |

---

### Destination Dataset

| Destination | Mood | Budget | Season | Rating |
|-------------|------|---------|---------|---------|
| Coorg | Stress Relief | Medium | Winter | 4.8 |
| Goa | Romantic | High | Winter | 4.9 |
| Manali | Adventure | Medium | Summer | 4.9 |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-Learn
- Matplotlib
- Joblib

---

## 🧠 Machine Learning Model

### Feature Engineering

TF-IDF Vectorizer

### Classification Algorithm

Logistic Regression

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 😊 Emotion to Mood Mapping

| Emotion | Travel Mood |
|----------|------------|
| anger | Stress Relief |
| sadness | Relaxation |
| fear | Safe Travel |
| joy | Excited |
| love | Romantic |
| surprise | Adventure |

---

## 📍 Sample Output

### User Input

I am exhausted from work and need some peace.

### Prediction

Emotion: sadness

Travel Mood: Relaxation

### Recommendations

- Alleppey
- Kumarakom
- Pondicherry
- Varkala

---

## 🔮 Future Enhancements

- Streamlit Web Application
- Real-Time Weather Integration
- Google Maps Integration
- Hotel Recommendation System
- Flight Recommendation System
- User Authentication
- Deep Learning Models (BERT)

---

## 👨‍💻 Author

Munaga Sriram

Aspiring Data Analyst | Machine Learning Enthusiast | NLP Learner
