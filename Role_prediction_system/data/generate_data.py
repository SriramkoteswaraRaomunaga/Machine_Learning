import os
import numpy as np
import pandas as pd

# Define skill categories and their individual skills (with new Web and Tool additions)
SKILL_CATEGORIES = {
    "Programming": ["Python", "Java", "C++", "SQL", "HTML_CSS", "JavaScript", "Go", "Rust"],
    "Web_Development": ["React", "Node_JS", "TypeScript", "Next_JS"],
    "Data_Visualization": ["Power_BI", "Tableau", "Excel"],
    "Databases": ["MySQL", "MongoDB", "PostgreSQL", "Redis", "Cassandra"],
    "Machine_Learning": ["Scikit_learn", "Regression", "Classification", "Clustering"],
    "Deep_Learning": ["TensorFlow", "PyTorch", "Keras", "CNNs", "RNNs"],
    "NLP": ["BERT", "GPT", "NLTK", "Spacy", "Transformers"],
    "Cloud": ["AWS", "Azure", "GCP", "Docker", "Kubernetes"],
    "Dev_Tools": ["Git", "Linux", "Agile", "REST_APIs"],
    "Soft_Skills": ["Communication", "Teamwork", "Problem_Solving", "Leadership", "Presentation"]
}

# Flatten to a single list of skills
ALL_SKILLS = []
for category, skills in SKILL_CATEGORIES.items():
    ALL_SKILLS.extend(skills)

# List of career roles to predict
ROLES = [
    "Data Scientist",
    "Machine Learning Engineer",
    "Data Analyst",
    "Software Engineer (Full-Stack)",
    "Cloud Architect / DevOps",
    "Database Administrator (DBA)",
    "NLP Engineer",
    "Product Manager"
]

# Set probabilities for each skill per role
P_HIGH = 0.85
P_MED_HIGH = 0.65
P_MED = 0.45
P_MED_LOW = 0.20
P_LOW = 0.05

# Skill profiles for each role mapping each skill to a probability
ROLE_PROB_MAPPING = {
    "Data Scientist": {
        "Python": P_HIGH, "SQL": P_HIGH, "Excel": P_MED_HIGH, "Tableau": P_MED_HIGH, "Power_BI": P_MED,
        "Scikit_learn": P_HIGH, "Regression": P_HIGH, "Classification": P_HIGH, "Clustering": P_HIGH,
        "TensorFlow": P_MED, "PyTorch": P_MED, "Keras": P_MED, "CNNs": P_MED_LOW, "RNNs": P_MED_LOW,
        "MySQL": P_MED, "PostgreSQL": P_MED_HIGH, "MongoDB": P_MED_LOW, "Redis": P_LOW, "Cassandra": P_LOW,
        "BERT": P_MED_LOW, "GPT": P_MED_LOW, "NLTK": P_MED_LOW, "Spacy": P_MED_LOW, "Transformers": P_MED_LOW,
        "AWS": P_MED_LOW, "Azure": P_LOW, "GCP": P_LOW, "Docker": P_MED_LOW, "Kubernetes": P_LOW,
        "Communication": P_HIGH, "Teamwork": P_MED_HIGH, "Problem_Solving": P_HIGH, "Leadership": P_MED, "Presentation": P_MED_HIGH,
        "Java": P_LOW, "C++": P_LOW, "HTML_CSS": P_LOW, "JavaScript": P_LOW, "Go": P_LOW, "Rust": P_LOW,
        # New Skills
        "React": P_LOW, "Node_JS": P_LOW, "TypeScript": P_LOW, "Next_JS": P_LOW,
        "Git": P_MED_HIGH, "Linux": P_MED, "Agile": P_MED_LOW, "REST_APIs": P_MED
    },
    "Machine Learning Engineer": {
        "Python": P_HIGH, "C++": P_MED_HIGH, "SQL": P_MED_HIGH, "Java": P_MED_LOW,
        "Scikit_learn": P_HIGH, "Regression": P_HIGH, "Classification": P_HIGH, "Clustering": P_HIGH,
        "TensorFlow": P_HIGH, "PyTorch": P_HIGH, "Keras": P_MED_HIGH, "CNNs": P_HIGH, "RNNs": P_HIGH,
        "BERT": P_MED, "GPT": P_MED, "NLTK": P_MED, "Spacy": P_MED, "Transformers": P_MED,
        "AWS": P_MED_HIGH, "Azure": P_MED, "GCP": P_MED, "Docker": P_HIGH, "Kubernetes": P_MED_HIGH,
        "MySQL": P_MED, "PostgreSQL": P_MED, "MongoDB": P_MED_LOW, "Redis": P_MED_LOW, "Cassandra": P_LOW,
        "Communication": P_MED_HIGH, "Teamwork": P_MED_HIGH, "Problem_Solving": P_HIGH, "Leadership": P_MED_LOW, "Presentation": P_MED_LOW,
        "HTML_CSS": P_LOW, "JavaScript": P_LOW, "Go": P_MED_LOW, "Rust": P_MED_LOW,
        "Excel": P_LOW, "Tableau": P_LOW, "Power_BI": P_LOW,
        # New Skills
        "React": P_MED_LOW, "Node_JS": P_MED_LOW, "TypeScript": P_MED_LOW, "Next_JS": P_LOW,
        "Git": P_HIGH, "Linux": P_HIGH, "Agile": P_MED, "REST_APIs": P_HIGH
    },
    "Data Analyst": {
        "SQL": P_HIGH, "Excel": P_HIGH, "Tableau": P_HIGH, "Power_BI": P_HIGH,
        "Python": P_MED_HIGH, "MySQL": P_MED_HIGH, "PostgreSQL": P_MED_HIGH,
        "Regression": P_MED, "Classification": P_MED_LOW, "Clustering": P_MED_LOW,
        "Communication": P_HIGH, "Teamwork": P_HIGH, "Problem_Solving": P_MED_HIGH, "Presentation": P_HIGH, "Leadership": P_MED,
        "Java": P_LOW, "C++": P_LOW, "HTML_CSS": P_LOW, "JavaScript": P_LOW, "Go": P_LOW, "Rust": P_LOW,
        "MongoDB": P_LOW, "Redis": P_LOW, "Cassandra": P_LOW, "Scikit_learn": P_LOW,
        "TensorFlow": P_LOW, "PyTorch": P_LOW, "Keras": P_LOW, "CNNs": P_LOW, "RNNs": P_LOW,
        "BERT": P_LOW, "GPT": P_LOW, "NLTK": P_LOW, "Spacy": P_LOW, "Transformers": P_LOW,
        "AWS": P_LOW, "Azure": P_LOW, "GCP": P_LOW, "Docker": P_LOW, "Kubernetes": P_LOW,
        # New Skills
        "React": P_LOW, "Node_JS": P_LOW, "TypeScript": P_LOW, "Next_JS": P_LOW,
        "Git": P_MED_LOW, "Linux": P_MED_LOW, "Agile": P_MED, "REST_APIs": P_MED_LOW
    },
    "Software Engineer (Full-Stack)": {
        "JavaScript": P_HIGH, "HTML_CSS": P_HIGH, "Java": P_HIGH, "Python": P_MED_HIGH, "C++": P_MED,
        "SQL": P_HIGH, "MySQL": P_HIGH, "PostgreSQL": P_HIGH, "MongoDB": P_MED_HIGH, "Redis": P_MED, "Cassandra": P_MED_LOW,
        "Docker": P_HIGH, "AWS": P_MED_HIGH, "Kubernetes": P_MED, "Go": P_MED_LOW, "Rust": P_MED_LOW,
        "Communication": P_MED_HIGH, "Teamwork": P_HIGH, "Problem_Solving": P_HIGH, "Leadership": P_MED_LOW, "Presentation": P_MED_LOW,
        "Excel": P_LOW, "Tableau": P_LOW, "Power_BI": P_LOW,
        "Scikit_learn": P_LOW, "Regression": P_LOW, "Classification": P_LOW, "Clustering": P_LOW,
        "TensorFlow": P_LOW, "PyTorch": P_LOW, "Keras": P_LOW, "CNNs": P_LOW, "RNNs": P_LOW,
        "BERT": P_LOW, "GPT": P_LOW, "NLTK": P_LOW, "Spacy": P_LOW, "Transformers": P_LOW,
        "Azure": P_MED_LOW, "GCP": P_MED_LOW,
        # New Skills
        "React": P_HIGH, "Node_JS": P_HIGH, "TypeScript": P_HIGH, "Next_JS": P_HIGH,
        "Git": P_HIGH, "Linux": P_MED_HIGH, "Agile": P_MED_HIGH, "REST_APIs": P_HIGH
    },
    "Cloud Architect / DevOps": {
        "AWS": P_HIGH, "Azure": P_MED_HIGH, "GCP": P_MED_HIGH, "Docker": P_HIGH, "Kubernetes": P_HIGH,
        "SQL": P_MED_HIGH, "MySQL": P_MED_HIGH, "PostgreSQL": P_MED_HIGH, "MongoDB": P_MED_LOW, "Redis": P_MED, "Cassandra": P_MED_LOW,
        "Python": P_MED_HIGH, "Java": P_MED_LOW, "Go": P_MED_HIGH, "Rust": P_MED, "C++": P_MED_LOW,
        "Problem_Solving": P_HIGH, "Teamwork": P_HIGH, "Communication": P_HIGH, "Leadership": P_MED_HIGH, "Presentation": P_MED,
        "JavaScript": P_MED_LOW, "HTML_CSS": P_MED_LOW,
        "Excel": P_LOW, "Tableau": P_LOW, "Power_BI": P_LOW,
        "Scikit_learn": P_LOW, "Regression": P_LOW, "Classification": P_LOW, "Clustering": P_LOW,
        "TensorFlow": P_LOW, "PyTorch": P_LOW, "Keras": P_LOW, "CNNs": P_LOW, "RNNs": P_LOW,
        "BERT": P_LOW, "GPT": P_LOW, "NLTK": P_LOW, "Spacy": P_LOW, "Transformers": P_LOW,
        # New Skills
        "React": P_MED, "Node_JS": P_MED, "TypeScript": P_MED, "Next_JS": P_MED_LOW,
        "Git": P_HIGH, "Linux": P_HIGH, "Agile": P_MED_HIGH, "REST_APIs": P_HIGH
    },
    "Database Administrator (DBA)": {
        "SQL": P_HIGH, "MySQL": P_HIGH, "PostgreSQL": P_HIGH, "MongoDB": P_HIGH, "Redis": P_HIGH, "Cassandra": P_HIGH,
        "Python": P_MED, "Java": P_MED_LOW, "AWS": P_MED_HIGH, "Azure": P_MED, "GCP": P_MED, "Docker": P_MED_HIGH, "Kubernetes": P_MED,
        "Problem_Solving": P_HIGH, "Teamwork": P_MED_HIGH, "Communication": P_MED_HIGH, "Leadership": P_MED, "Presentation": P_MED_LOW,
        "C++": P_LOW, "JavaScript": P_LOW, "HTML_CSS": P_LOW, "Go": P_LOW, "Rust": P_LOW,
        "Excel": P_MED_LOW, "Tableau": P_LOW, "Power_BI": P_LOW,
        "Scikit_learn": P_LOW, "Regression": P_LOW, "Classification": P_LOW, "Clustering": P_LOW,
        "TensorFlow": P_LOW, "PyTorch": P_LOW, "Keras": P_LOW, "CNNs": P_LOW, "RNNs": P_LOW,
        "BERT": P_LOW, "GPT": P_LOW, "NLTK": P_LOW, "Spacy": P_LOW, "Transformers": P_LOW,
        # New Skills
        "React": P_LOW, "Node_JS": P_LOW, "TypeScript": P_LOW, "Next_JS": P_LOW,
        "Git": P_MED_HIGH, "Linux": P_HIGH, "Agile": P_MED, "REST_APIs": P_MED
    },
    "NLP Engineer": {
        "Python": P_HIGH, "PyTorch": P_HIGH, "TensorFlow": P_HIGH, "NLTK": P_HIGH, "Spacy": P_HIGH, "BERT": P_HIGH, "Transformers": P_HIGH, "GPT": P_HIGH,
        "SQL": P_MED, "Scikit_learn": P_HIGH, "Regression": P_MED_HIGH, "Classification": P_HIGH, "Clustering": P_MED_HIGH,
        "CNNs": P_HIGH, "RNNs": P_HIGH, "Keras": P_MED, "Docker": P_MED_HIGH, "AWS": P_MED, "Kubernetes": P_MED_LOW,
        "Communication": P_MED_HIGH, "Teamwork": P_MED_HIGH, "Problem_Solving": P_HIGH, "Presentation": P_MED, "Leadership": P_MED_LOW,
        "Java": P_LOW, "C++": P_LOW, "HTML_CSS": P_LOW, "JavaScript": P_LOW, "Go": P_LOW, "Rust": P_LOW,
        "Excel": P_LOW, "Tableau": P_LOW, "Power_BI": P_LOW,
        "MySQL": P_LOW, "PostgreSQL": P_LOW, "MongoDB": P_LOW, "Redis": P_LOW, "Cassandra": P_LOW,
        "Azure": P_LOW, "GCP": P_LOW,
        # New Skills
        "React": P_MED_LOW, "Node_JS": P_MED_LOW, "TypeScript": P_MED_LOW, "Next_JS": P_LOW,
        "Git": P_HIGH, "Linux": P_HIGH, "Agile": P_MED, "REST_APIs": P_MED_HIGH
    },
    "Product Manager": {
        "Communication": P_HIGH, "Teamwork": P_HIGH, "Problem_Solving": P_HIGH, "Leadership": P_HIGH, "Presentation": P_HIGH,
        "Excel": P_HIGH, "SQL": P_MED_HIGH, "Tableau": P_MED, "Power_BI": P_MED,
        "Python": P_MED_LOW,
        "Java": P_LOW, "C++": P_LOW, "HTML_CSS": P_LOW, "JavaScript": P_LOW, "Go": P_LOW, "Rust": P_LOW,
        "MySQL": P_LOW, "MongoDB": P_LOW, "PostgreSQL": P_LOW, "Redis": P_LOW, "Cassandra": P_LOW,
        "Scikit_learn": P_LOW, "Regression": P_LOW, "Classification": P_LOW, "Clustering": P_LOW,
        "TensorFlow": P_LOW, "PyTorch": P_LOW, "Keras": P_LOW, "CNNs": P_LOW, "RNNs": P_LOW,
        "BERT": P_LOW, "GPT": P_LOW, "NLTK": P_LOW, "Spacy": P_LOW, "Transformers": P_LOW,
        "AWS": P_LOW, "Azure": P_LOW, "GCP": P_LOW, "Docker": P_LOW, "Kubernetes": P_LOW,
        # New Skills
        "React": P_MED_LOW, "Node_JS": P_MED_LOW, "TypeScript": P_MED_LOW, "Next_JS": P_MED_LOW,
        "Git": P_MED_LOW, "Linux": P_LOW, "Agile": P_HIGH, "REST_APIs": P_MED_LOW
    }
}

# Setup generation seed
np.random.seed(42)

def generate_synthetic_dataset(num_samples_per_role=250):
    data = []
    
    for role in ROLES:
        probs = ROLE_PROB_MAPPING[role]
        for _ in range(num_samples_per_role):
            row = {}
            for skill in ALL_SKILLS:
                p = probs.get(skill, P_LOW)
                p_noise = np.clip(p + np.random.normal(0, 0.05), 0.01, 0.99)
                row[skill] = int(np.random.rand() < p_noise)
                
            row["Role"] = role
            data.append(row)
            
    df = pd.DataFrame(data)
    df = df.sample(frac=1.0).reset_index(drop=True)
    return df

if __name__ == "__main__":
    print("Generating synthetic skills dataset (including new Web & Tool skills)...")
    df = generate_synthetic_dataset(num_samples_per_role=250)
    
    os.makedirs("data", exist_ok=True)
    output_path = os.path.join("data", "skills_dataset.csv")
    df.to_csv(output_path, index=False)
    
    print(f"Dataset generated successfully at: {output_path}")
    print(f"Shape of dataset: {df.shape}")
    print("\nRole distribution:")
    print(df["Role"].value_counts())
