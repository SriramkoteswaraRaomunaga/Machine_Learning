import streamlit as st

def apply_custom_styles():
    """Injects custom CSS into Streamlit to create a premium, modern dashboard UI."""
    css = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <style>
        /* Global Font Override */
        html, body, [class*="css"], .stMarkdown, p, span, div, label {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* Modern Glassmorphic Container Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 40px 0 rgba(142, 68, 173, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        
        /* Light mode fallback or adjustment if needed */
        [data-theme="light"] .glass-card {
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(0, 0, 0, 0.08);
            box-shadow: 0 8px 24px 0 rgba(0, 0, 0, 0.05);
        }
        [data-theme="light"] .glass-card:hover {
            box-shadow: 0 12px 30px 0 rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(0, 0, 0, 0.12);
        }

        /* Gradient Heading */
        .gradient-text {
            background: linear-gradient(135deg, #FF6B6B 0%, #8E2DE2 50%, #4A00E0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            margin-bottom: 10px;
        }
        
        .gradient-text-blue {
            background: linear-gradient(135deg, #00C6FF 0%, #0072FF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .gradient-text-green {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            margin-bottom: 10px;
        }

        /* Metric Cards styling */
        .premium-metric {
            text-align: center;
            padding: 15px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        
        .premium-metric-value {
            font-size: 2.2rem;
            font-weight: 700;
            color: #8E2DE2;
            margin: 5px 0;
            text-shadow: 0 0 10px rgba(142, 68, 173, 0.3);
        }
        
        .premium-metric-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: rgba(255, 255, 255, 0.6);
        }

        /* Custom Skill Badges */
        .badge-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }
        
        .badge-skill {
            background: rgba(142, 68, 173, 0.12);
            color: #d1a3ff;
            border: 1px solid rgba(142, 68, 173, 0.4);
            border-radius: 20px;
            padding: 4px 12px;
            font-size: 0.85rem;
            font-weight: 500;
            display: inline-block;
        }

        .badge-missing {
            background: rgba(231, 76, 60, 0.12);
            color: #ff9999;
            border: 1px solid rgba(231, 76, 60, 0.4);
            border-radius: 20px;
            padding: 4px 12px;
            font-size: 0.85rem;
            font-weight: 500;
            display: inline-block;
        }
        
        .badge-matching {
            background: rgba(46, 204, 113, 0.12);
            color: #99ffa9;
            border: 1px solid rgba(46, 204, 113, 0.4);
            border-radius: 20px;
            padding: 4px 12px;
            font-size: 0.85rem;
            font-weight: 500;
            display: inline-block;
        }

        /* Custom sidebar styling */
        .css-1542g7k, .css-6q9mec {
            background-color: #0c0f18 !important;
        }
        
        /* Modernized Streamlit Alert Boxes */
        .stAlert {
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(5px);
        }
        
        /* Subtitle */
        .subtitle {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.7);
            margin-top: -10px;
            margin-bottom: 25px;
            font-weight: 300;
        }
        
        /* Interactive Pill selection indicator */
        .category-title {
            font-size: 1.15rem;
            font-weight: 600;
            margin-top: 15px;
            margin-bottom: 8px;
            color: #E2E2E2;
            border-left: 3px solid #8E2DE2;
            padding-left: 8px;
        }

        /* Custom road map layout */
        .roadmap-card {
            border-left: 4px solid #8E2DE2;
            background: rgba(255, 255, 255, 0.02);
            padding: 15px;
            border-radius: 0 12px 12px 0;
            margin-bottom: 12px;
        }
        
        .roadmap-card h5 {
            margin: 0 0 5px 0;
            color: #E2E2E2;
            font-weight: 600;
        }
        
        .roadmap-card p {
            margin: 0 0 10px 0;
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
