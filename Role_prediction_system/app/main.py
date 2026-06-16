import json
import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from styles import apply_custom_styles
from roadmap_data import SKILL_ROADMAPS

# Page Config
st.set_page_config(
    page_title="AI Career Path Predictor & Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply premium styles
apply_custom_styles()

# Skill Categorization Mapping (with Web Development and Developer Tools additions)
SKILL_CATEGORIES = {
    "Programming 💻": ["Python", "Java", "C++", "SQL", "HTML_CSS", "JavaScript", "Go", "Rust"],
    "Web Development 🌐": ["React", "Node_JS", "TypeScript", "Next_JS"],
    "Data Visualization 📊": ["Power_BI", "Tableau", "Excel"],
    "Databases 🗄️": ["MySQL", "MongoDB", "PostgreSQL", "Redis", "Cassandra"],
    "Machine Learning 🤖": ["Scikit_learn", "Regression", "Classification", "Clustering"],
    "Deep Learning 🧠": ["TensorFlow", "PyTorch", "Keras", "CNNs", "RNNs"],
    "NLP 🗣️": ["BERT", "GPT", "NLTK", "Spacy", "Transformers"],
    "Cloud & DevOps ☁️": ["AWS", "Azure", "GCP", "Docker", "Kubernetes"],
    "Developer Tools & Methods 🛠️": ["Git", "Linux", "Agile", "REST_APIs"],
    "Soft Skills 🤝": ["Communication", "Teamwork", "Problem_Solving", "Leadership", "Presentation"]
}

# Cache model and metadata loading with cache invalidation on file modifications
@st.cache_resource
def load_ml_resources(model_mtime, metadata_mtime):
    model_path = os.path.join("models", "model.joblib")
    metadata_path = os.path.join("models", "model_metadata.json")
    
    if not os.path.exists(model_path) or not os.path.exists(metadata_path):
        return None, None
        
    model = joblib.load(model_path)
    with open(metadata_path, "r") as f:
        metadata = json.load(f)
        
    return model, metadata

@st.cache_data
def load_skills_dataset(dataset_mtime):
    dataset_path = os.path.join("data", "skills_dataset.csv")
    if os.path.exists(dataset_path):
        return pd.read_csv(dataset_path)
    return None

# Load Resources with file system watches
model_path = os.path.join("models", "model.joblib")
metadata_path = os.path.join("models", "model_metadata.json")
dataset_path = os.path.join("data", "skills_dataset.csv")

model_mtime = os.path.getmtime(model_path) if os.path.exists(model_path) else 0
metadata_mtime = os.path.getmtime(metadata_path) if os.path.exists(metadata_path) else 0
dataset_mtime = os.path.getmtime(dataset_path) if os.path.exists(dataset_path) else 0

model, metadata = load_ml_resources(model_mtime, metadata_mtime)
dataset = load_skills_dataset(dataset_mtime)

# Title and Banner
st.markdown("<h1 class='gradient-text'>🎯 AI-Powered Career Path & Skill Gap Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Navigate your career journey: Predict ideal roles, analyze skills, and get personalized study paths.</p>", unsafe_allow_html=True)

if model is None or metadata is None or dataset is None:
    st.error("⚠️ Model or dataset files not found. Please run the data generation and training scripts first.")
    st.info("Execute: `python data/generate_data.py` and `python models/train.py` in your terminal.")
    st.stop()

# Sidebar Info
st.sidebar.markdown("### About the System")
st.sidebar.write(
    "This system uses a **Random Forest Classifier** trained on synthetic IT skill profiles "
    "to recommend the top matching career roles and compute skill gaps."
)
app_mode = "Career Predictor & Gap Analyzer"

# Helper function to get clean display names for skills (replace underscore with space/slash)
def clean_skill_name(name):
    return name.replace("_", " / ")

# ----------------- MAIN APP MODE 1: PREDICTOR & GAP ANALYZER -----------------
if app_mode == "Career Predictor & Gap Analyzer":
    
    # Initialize version counter and presets in session state
    if "form_clear_counter" not in st.session_state:
        st.session_state["form_clear_counter"] = 0
        
    for cat_name in SKILL_CATEGORIES.keys():
        preset_key = f"preset_{cat_name}"
        if preset_key not in st.session_state:
            st.session_state[preset_key] = []
                
    if "prediction_skills" not in st.session_state:
        st.session_state["prediction_skills"] = None
        
    # Preset Profile Buttons
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### ⚡ Quick Demo: Pre-fill a Candidate Profile")
    col_pre1, col_pre2, col_pre3, col_pre4 = st.columns(4)
    
    preset_profile = None
    if col_pre1.button("🧠 Data Scientist Profile", use_container_width=True):
        preset_profile = ["Python", "SQL", "Excel", "Tableau", "Scikit_learn", "Regression", "Classification", "Communication", "Problem_Solving", "Presentation", "Git", "Linux", "REST_APIs"]
    if col_pre2.button("🚀 ML Engineer Profile", use_container_width=True):
        preset_profile = ["Python", "C++", "SQL", "Scikit_learn", "Regression", "Classification", "TensorFlow", "PyTorch", "Docker", "Kubernetes", "Problem_Solving", "Git", "Linux", "REST_APIs"]
    if col_pre3.button("💻 Full-Stack Dev Profile", use_container_width=True):
        preset_profile = ["JavaScript", "HTML_CSS", "Java", "Python", "SQL", "MySQL", "PostgreSQL", "MongoDB", "Docker", "Teamwork", "Problem_Solving", "React", "Node_JS", "TypeScript", "Next_JS", "Git", "REST_APIs"]
    if col_pre4.button("🧹 Clear All Selections", use_container_width=True):
        preset_profile = []
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Handle preset selection
    if preset_profile is not None:
        for cat_name, skills_list in SKILL_CATEGORIES.items():
            preset_key = f"preset_{cat_name}"
            # Filter and convert preset skills to display name format
            st.session_state[preset_key] = [clean_skill_name(s) for s in skills_list if s in preset_profile]
            
        # Recreate multiselects with empty/new default lists
        st.session_state["form_clear_counter"] += 1
        
        if not preset_profile:
            st.session_state["prediction_skills"] = None
        else:
            st.session_state["prediction_skills"] = preset_profile
            
        st.rerun()
        
    # Form for input
    with st.form("skills_form"):
        st.markdown("### 🛠️ Select Your Skills")
        st.write("Choose all the skills you currently possess from the dropdowns below:")
        
        # Grid layout for skill categories
        cat_cols = st.columns(2)
        categories_keys = list(SKILL_CATEGORIES.keys())
        
        # Current version suffix
        widget_suffix = st.session_state["form_clear_counter"]
        
        for idx, cat_name in enumerate(categories_keys):
            col_target = cat_cols[idx % 2]
            with col_target:
                skills_list = SKILL_CATEGORIES[cat_name]
                clean_skills_list = [clean_skill_name(s) for s in skills_list]
                
                # Bind multiselect defaults to session state presets
                default_val = st.session_state.get(f"preset_{cat_name}", [])
                
                st.multiselect(
                    label=cat_name,
                    options=clean_skills_list,
                    default=default_val,
                    key=f"ms_{cat_name}_{widget_suffix}"
                )
                        
        submit_btn = st.form_submit_button("Analyze My Career Fit 🚀", use_container_width=True)

    # Action on form submission
    if submit_btn:
        selected_skills = []
        widget_suffix = st.session_state["form_clear_counter"]
        
        for cat_name, skills_list in SKILL_CATEGORIES.items():
            ms_key = f"ms_{cat_name}_{widget_suffix}"
            selected_names = st.session_state.get(ms_key, [])
            for name in selected_names:
                orig_key = next((s for s in skills_list if clean_skill_name(s) == name), None)
                if orig_key:
                    selected_skills.append(orig_key)
                    
        if not selected_skills:
            st.warning("⚠️ Please select at least one skill to analyze your profile.")
            st.session_state["prediction_skills"] = None
        else:
            # Store selected skills in session state for displaying results
            st.session_state["prediction_skills"] = selected_skills
            
            # Clear preset values in session state
            for cat_name in SKILL_CATEGORIES.keys():
                st.session_state[f"preset_{cat_name}"] = []
                
            # Recreate multiselects on rerun with empty lists
            st.session_state["form_clear_counter"] += 1
                    
            # Rerun so UI resets inputs but retains predicted results
            st.rerun()

    # If there are predictions to display
    if st.session_state.get("prediction_skills"):
        selected_skills = st.session_state["prediction_skills"]
        
        # PREDICTION LOGIC
        # Build input vector
        input_vector = []
        for skill in metadata["skills"]:
            input_vector.append(1 if skill in selected_skills else 0)
            
        input_vector = np.array(input_vector).reshape(1, -1)
        
        # Predict probabilities
        probabilities = model.predict_proba(input_vector)[0]
        classes = model.classes_
        
        # Get top 3 roles and their scores
        pred_indices = np.argsort(probabilities)[::-1][:3]
        top_roles = [(classes[idx], probabilities[idx]) for idx in pred_indices]
        
        primary_role = top_roles[0][0]
        primary_score = top_roles[0][1]
        
        # Render predictions header
        st.markdown("<h2 class='gradient-text-blue'>📊 Profile Analysis Results</h2>", unsafe_allow_html=True)
        
        # Three Columns for Top Predictions
        col_pred1, col_pred2 = st.columns([1, 1.2])
        
        with col_pred1:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("### Top Career Matches")
            
            # Bar chart for confidence scores
            chart_roles = [clean_skill_name(r[0]) for r in top_roles]
            chart_scores = [round(r[1] * 100, 1) for r in top_roles]
            
            fig = px.bar(
                x=chart_scores,
                y=chart_roles,
                orientation='h',
                text=[f"{s}%" for s in chart_scores],
                labels={'x': 'Confidence Score (%)', 'y': 'Career Role'},
                color=chart_scores,
                color_continuous_scale='Purples'
            )
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E0E0E0',
                xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', range=[0, 105]),
                yaxis=dict(autorange="reversed"),
                coloraxis_showscale=False,
                height=280,
                margin=dict(l=0, r=0, t=10, b=0)
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_pred2:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown(f"### Role Alignment: **{primary_role}**")
            
            # Fetch typical role requirements from dataset
            role_data = dataset[dataset["Role"] == primary_role].drop(columns=["Role"])
            role_averages = role_data.mean()
            
            # Define benchmark (skills present in >= 45% of profiles in dataset for that role)
            required_skills = role_averages[role_averages >= 0.45].index.tolist()
            
            # Calculate career readiness score
            matching_required = [s for s in selected_skills if s in required_skills]
            readiness_score = int((len(matching_required) / len(required_skills)) * 100) if required_skills else 0
            
            # Show radial gauge for readiness score
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = readiness_score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Career Readiness Score", 'font': {'size': 18, 'color': '#E0E0E0'}},
                number = {'suffix': "%", 'font': {'color': '#8E2DE2', 'size': 44}},
                gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#8E2DE2"},
                    'bar': {'color': "#8E2DE2"},
                    'bgcolor': "rgba(255, 255, 255, 0.05)",
                    'borderwidth': 1,
                    'bordercolor': "rgba(255, 255, 255, 0.1)",
                    'steps': [
                        {'range': [0, 50], 'color': 'rgba(231, 76, 60, 0.1)'},
                        {'range': [50, 80], 'color': 'rgba(241, 196, 15, 0.1)'},
                        {'range': [80, 100], 'color': 'rgba(46, 204, 113, 0.1)'}
                    ]
                }
            ))
            fig_gauge.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#E0E0E0',
                height=260,
                margin=dict(l=20, r=20, t=40, b=0)
            )
            st.plotly_chart(fig_gauge, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        # GAP ANALYSIS SECTION
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Skill Gap Details")
        
        # Partition user skills
        user_matching = [s for s in required_skills if s in selected_skills]
        user_missing = [s for s in required_skills if s not in selected_skills]
        user_extra = [s for s in selected_skills if s not in required_skills]
        
        col_gap1, col_gap2 = st.columns([1.2, 1])
        
        with col_gap1:
            # Grouped bar chart comparing user skill value (0/1) vs industry average (%)
            all_eval_skills = sorted(list(set(required_skills + selected_skills)))
            
            user_values = [100 if s in selected_skills else 0 for s in all_eval_skills]
            industry_values = [round(role_averages[s] * 100, 1) for s in all_eval_skills]
            display_labels = [clean_skill_name(s) for s in all_eval_skills]
            
            fig_gap = go.Figure(data=[
                go.Bar(name='Your Skill Level', x=display_labels, y=user_values, marker_color='#8E2DE2'),
                go.Bar(name='Industry Average', x=display_labels, y=industry_values, marker_color='rgba(255, 255, 255, 0.3)')
            ])
            fig_gap.update_layout(
                barmode='group',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E0E0E0',
                xaxis=dict(showgrid=False),
                yaxis=dict(title="Skill Proficiency (%)", showgrid=True, gridcolor='rgba(255,255,255,0.05)', range=[0, 105]),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                height=350,
                margin=dict(l=0, r=0, t=10, b=0)
            )
            st.plotly_chart(fig_gap, use_container_width=True)
            
        with col_gap2:
            # Badges Layout
            st.write("**Matching Required Skills** (You have these!)")
            if user_matching:
                st.markdown("<div class='badge-container'>" + "".join([f"<span class='badge-matching'>{clean_skill_name(s)}</span>" for s in user_matching]) + "</div>", unsafe_allow_html=True)
            else:
                st.write("None")
                
            st.markdown("<br>", unsafe_allow_html=True)
            st.write("**Skills Gap** (Industry requires these, but you lack them!)")
            if user_missing:
                st.markdown("<div class='badge-container'>" + "".join([f"<span class='badge-missing'>{clean_skill_name(s)}</span>" for s in user_missing]) + "</div>", unsafe_allow_html=True)
            else:
                st.success("🎉 Outstanding! You have no skill gaps for this role!")
                
            st.markdown("<br>", unsafe_allow_html=True)
            st.write("**Extra Skills** (Valuable complementary skills you possess)")
            if user_extra:
                st.markdown("<div class='badge-container'>" + "".join([f"<span class='badge-skill'>{clean_skill_name(s)}</span>" for s in user_extra]) + "</div>", unsafe_allow_html=True)
            else:
                st.write("None")
                
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Personalized learning roadmap and diagnostics page are hidden/removed per request
        pass
