# A rich database of high-quality educational resources, certifications, and project ideas for all 48 skills.

SKILL_ROADMAPS = {
    # programming
    "Python": {
        "duration": "3-4 Weeks",
        "courses": ["Python for Everybody (Coursera - University of Michigan)", "Complete Python Bootcamp (Udemy - Jose Portilla)"],
        "books": ["Python Crash Course by Eric Matthes", "Fluent Python by Luciano Ramalho"],
        "projects": ["Build an automated web scraper and API", "Develop a Command-Line Todo application with database storage"]
    },
    "Java": {
        "duration": "4-6 Weeks",
        "courses": ["Java Programming and Software Engineering Fundamentals (Coursera - Duke University)", "Java 17 Masterclass: Start Coding in 2024 (Udemy)"],
        "books": ["Effective Java by Joshua Bloch", "Head First Java by Kathy Sierra"],
        "projects": ["Build a full-fledged REST API using Spring Boot", "Create a desktop inventory system with GUI"]
    },
    "C++": {
        "duration": "6-8 Weeks",
        "courses": ["Beginning C++ Programming - From Beginner to Beyond (Udemy)", "C++ Nanodegree (Udacity)"],
        "books": ["Programming: Principles and Practice Using C++ by Bjarne Stroustrup", "Effective Modern C++ by Scott Meyers"],
        "projects": ["Build a low-latency 2D game engine", "Develop a custom memory manager or file system parser"]
    },
    "SQL": {
        "duration": "2-3 Weeks",
        "courses": ["SQL for Data Science (Coursera - UC Davis)", "The Ultimate MySQL Bootcamp (Udemy)"],
        "books": ["SQL Queries for Mere Mortals by John L. Viescas", "Learning SQL by Alan Beaulieu"],
        "projects": ["Write complex analytical queries on database dumps", "Optimize slow-running database queries with indexing"]
    },
    "HTML_CSS": {
        "duration": "2 Weeks",
        "courses": ["HTML and CSS Design and Build Websites (Book/Resource)", "Responsive Web Design (freeCodeCamp)"],
        "books": ["HTML and CSS: Design and Build Websites by Jon Duckett"],
        "projects": ["Design a responsive portfolio website", "Recreate a landing page using modern CSS Grid and Flexbox"]
    },
    "JavaScript": {
        "duration": "3-5 Weeks",
        "courses": ["The Complete JavaScript Course: From Zero to Expert (Udemy)", "JavaScript: The Advanced Concepts (ZTM Academy)"],
        "books": ["You Don't Know JS by Kyle Simpson", "Eloquent JavaScript by Marijn Haverbeke"],
        "projects": ["Create a dynamic Kanban Board app using vanilla JS", "Build an interactive music synthesizer app"]
    },
    "Go": {
        "duration": "3-4 Weeks",
        "courses": ["Programming with Google Go (Coursera - UC Irvine)", "Learn Go (Codecademy)"],
        "books": ["The Go Programming Language by Alan A. A. Donovan", "Go in Action by William Kennedy"],
        "projects": ["Develop a highly concurrent TCP chat server", "Build a microservice that exposes a gRPC interface"]
    },
    "Rust": {
        "duration": "6-8 Weeks",
        "courses": ["Rust Programming Course (Udemy)", "Ultimate Rust Crash Course (Udemy)"],
        "books": ["The Rust Programming Language (official docs)", "Programming Rust by Jim Blandy"],
        "projects": ["Write a command-line search tool (like grep) in Rust", "Create a thread-safe custom key-value store"]
    },
    # web development (NEW)
    "React": {
        "duration": "3-4 Weeks",
        "courses": ["React - The Complete Guide (Udemy - Maximilian Schwarzmüller)", "Modern React with Redux (Udemy)"],
        "books": ["The Road to React by Robin Wieruch"],
        "projects": ["Build an interactive social media feed dashboard", "Create a dynamic task management board (Trello clone)"]
    },
    "Node_JS": {
        "duration": "3-4 Weeks",
        "courses": ["The Complete Node.js Developer Course (Udemy - Andrew Mead)", "Node.js, Express, MongoDB & More (Udemy)"],
        "books": ["Node.js Design Patterns by Mario Casciaro"],
        "projects": ["Build a real-time messaging server using WebSockets", "Create an scalable API gateway handling authorization and logs"]
    },
    "TypeScript": {
        "duration": "2 Weeks",
        "courses": ["Understanding TypeScript (Udemy - Maximilian Schwarzmüller)", "TypeScript Design Patterns (Udemy)"],
        "books": ["Programming TypeScript by Boris Cherny"],
        "projects": ["Refactor a JavaScript project to TypeScript with strict type configs", "Develop type-safe API schema definitions"]
    },
    "Next_JS": {
        "duration": "3 Weeks",
        "courses": ["Next.js 14 HTML/CSS & React (Udemy)", "Next.js Complete Guide (Udemy)"],
        "books": ["Next.js official documentation & tutorials"],
        "projects": ["Build a server-side rendered (SSR) e-commerce portal", "Create a static markdown blog utilizing App Router and Incremental Static Regeneration"]
    },
    # data visualization
    "Power_BI": {
        "duration": "2-3 Weeks",
        "courses": ["Microsoft Power BI Data Analyst Professional Certificate (Coursera)", "PL-300 Exam Prep (Udemy)"],
        "books": ["Analyzing Data with Power BI and Power Pivot for Excel by Alberto Ferrari"],
        "projects": ["Create an executive-level performance dashboard", "Connect and clean multiple dirty CSV datasets using Power Query"]
    },
    "Tableau": {
        "duration": "2-3 Weeks",
        "courses": ["Tableau 2024 A-Z: Hands-On Tableau Training (Udemy)", "Data Visualization with Tableau Specialization (Coursera)"],
        "books": ["Practical Tableau by Ryan Sleeper", "Communicating Data with Tableau by Ben Jones"],
        "projects": ["Build an interactive storytelling dashboard using COVID-19 dataset", "Construct dynamic maps and cohort charts"]
    },
    "Excel": {
        "duration": "1-2 Weeks",
        "courses": ["Excel Skills for Business Specialization (Coursera - Macquarie)", "Microsoft Excel - Excel from Beginner to Advanced (Udemy)"],
        "books": ["Ctrl+Shift+Enter: Mastering Excel Array Formulas by Mike Girvin"],
        "projects": ["Create a fully automated financial model using PivotTables", "Implement complex logical macros and VBA operations"]
    },
    # databases
    "MySQL": {
        "duration": "2 Weeks",
        "courses": ["MySQL for Database Administrators (Oracle University)", "Database Design with MySQL (Udemy)"],
        "books": ["High Performance MySQL by Silvia Botros"],
        "projects": ["Design and normalize an e-commerce schema", "Implement custom backup/recovery scripts and database triggers"]
    },
    "MongoDB": {
        "duration": "2-3 Weeks",
        "courses": ["MongoDB Basics (MongoDB University)", "Complete MongoDB Developer Course (Udemy)"],
        "books": ["MongoDB: The Definitive Guide by Shannon Bradshaw"],
        "projects": ["Build a NoSQL database backend for a blog application", "Implement complex aggregation pipelines on high-volume logs"]
    },
    "PostgreSQL": {
        "duration": "2-3 Weeks",
        "courses": ["PostgreSQL: Bootcamp to Advanced (Udemy)", "SQL and PostgreSQL: The Complete Developer's Guide (Udemy)"],
        "books": ["PostgreSQL: Up and Running by Regina O. Obe"],
        "projects": ["Design a geospatial backend utilizing PostGIS extension", "Configure database partitioning and custom full-text search index"]
    },
    "Redis": {
        "duration": "1-2 Weeks",
        "courses": ["Redis University (RU101: Introduction to Redis Data Structures)"],
        "books": ["Redis in Action by Josiah L. Carlson"],
        "projects": ["Build an in-memory session store & cache layer for a web app", "Implement a pub-sub real-time event router"]
    },
    "Cassandra": {
        "duration": "3-4 Weeks",
        "courses": ["Apache Cassandra Administrator Course (Datastax Academy)"],
        "books": ["Cassandra: The Definitive Guide by Jeff Carpenter"],
        "projects": ["Design a wide-column table schema for time-series IoT data", "Set up a multi-node Cassandra cluster locally"]
    },
    # machine learning
    "Scikit_learn": {
        "duration": "3-4 Weeks",
        "courses": ["Machine Learning with Python (Coursera - IBM)", "Applied Machine Learning in Python (Coursera - UMichigan)"],
        "books": ["Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron"],
        "projects": ["Build an end-to-end churn prediction pipeline", "Deploy a classification API using Scikit-learn and Flask"]
    },
    "Regression": {
        "duration": "1-2 Weeks",
        "courses": ["Linear Regression and Modeling (Coursera - Duke)", "Mathematics for Machine Learning: Linear Algebra (Coursera)"],
        "books": ["Introduction to Linear Regression Analysis by Douglas C. Montgomery"],
        "projects": ["Predict housing prices with Ridge, Lasso, and ElasticNet", "Conduct regression diagnostic checks (multicollinearity, residuals)"]
    },
    "Classification": {
        "duration": "1-2 Weeks",
        "courses": ["Classification Models in Python (Coursera)", "Supervised Machine Learning: Regression and Classification (Coursera)"],
        "books": ["Pattern Recognition and Machine Learning by Christopher Bishop"],
        "projects": ["Classify medical images or customer behaviors", "Build a credit card fraud detection system dealing with imbalanced classes"]
    },
    "Clustering": {
        "duration": "1-2 Weeks",
        "courses": ["Unsupervised Learning, Recommenders, Reinforcement Learning (Coursera - Andrew Ng)"],
        "books": ["Introduction to Statistical Learning by Gareth James"],
        "projects": ["Perform customer segmentation on transaction histories", "Develop a news article grouping engine using K-means and PCA"]
    },
    # deep learning
    "TensorFlow": {
        "duration": "4-6 Weeks",
        "courses": ["Deep Learning Specialization (Coursera - DeepLearning.AI)", "TensorFlow Developer Professional Certificate (Coursera)"],
        "books": ["Deep Learning with Python by François Chollet"],
        "projects": ["Implement custom training loops for GANs using TF", "Build a neural machine translation engine"]
    },
    "PyTorch": {
        "duration": "4-6 Weeks",
        "courses": ["PyTorch for Deep Learning Bootcamp (Udemy)", "Deep Neural Networks with PyTorch (Coursera)"],
        "books": ["Deep Learning with PyTorch by Eli Stevens"],
        "projects": ["Train a ResNet model from scratch on CIFAR-10", "Implement a custom neural style transfer script"]
    },
    "Keras": {
        "duration": "2 Weeks",
        "courses": ["Deep Learning with Keras (Coursera)", "Introduction to Deep Learning with Keras (Udemy)"],
        "books": ["Deep Learning with Python (2nd Edition) by François Chollet"],
        "projects": ["Build and train a simple CNN for handwritten digit recognition", "Develop a regression model for tabular predictions"]
    },
    "CNNs": {
        "duration": "2-3 Weeks",
        "courses": ["Convolutional Neural Networks (Coursera - DeepLearning.AI)"],
        "books": ["Computer Vision: Algorithms and Applications by Richard Szeliski"],
        "projects": ["Fine-tune a MobileNet model for custom object classification", "Build a semantic segmentation network (U-Net) for medical scans"]
    },
    "RNNs": {
        "duration": "2-3 Weeks",
        "courses": ["Sequence Models (Coursera - DeepLearning.AI)"],
        "books": ["Speech and Language Processing by Daniel Jurafsky"],
        "projects": ["Develop an LSTM text generation engine", "Build a stock price forecasting model using GRU network"]
    },
    # nlp
    "BERT": {
        "duration": "3-4 Weeks",
        "courses": ["Hugging Face NLP Course (Hugging Face Academy)", "Natural Language Processing Specialization (Coursera)"],
        "books": ["Natural Language Processing with Transformers by Lewis Tunstall"],
        "projects": ["Fine-tune BERT for aspect-based sentiment analysis", "Use BERT for question answering over custom PDF documentation"]
    },
    "GPT": {
        "duration": "3-4 Weeks",
        "courses": ["Generative AI with Large Language Models (Coursera - DeepLearning.AI)"],
        "books": ["Architectures of LLMs (Hugging Face Documentation)"],
        "projects": ["Build an autonomous task agent using GPT-4 API", "Fine-tune GPT-2/3 locally on a custom conversational dataset"]
    },
    "NLTK": {
        "duration": "1-2 Weeks",
        "courses": ["Natural Language Processing with Python (NLTK Book Course)"],
        "books": ["Natural Language Processing with Python by Steven Bird"],
        "projects": ["Develop an automated text summarizer using word frequencies", "Construct a regex-based parser for resume information extraction"]
    },
    "Spacy": {
        "duration": "1-2 Weeks",
        "courses": ["Advanced NLP with spaCy (Official Interactive Course)"],
        "books": ["spaCy in Action by Yuli Vasiliev"],
        "projects": ["Build a custom Named Entity Recognition model for financial news", "Set up a text classification pipeline for support tickets"]
    },
    "Transformers": {
        "duration": "3-4 Weeks",
        "courses": ["Hugging Face Transformers Course", "NLP with Transformers (Udemy)"],
        "books": ["Natural Language Processing with Transformers by Lewis Tunstall"],
        "projects": ["Deploy a pipeline using Hugging Face pipelines for translation", "Implement text summarization with T5 or BART"]
    },
    # cloud
    "AWS": {
        "duration": "4-6 Weeks",
        "courses": ["AWS Certified Solutions Architect Associate (Udemy - Stephane Maarek)", "AWS Cloud Practitioner Essentials (edX)"],
        "books": ["AWS Certified Solutions Architect Official Study Guide"],
        "projects": ["Build a serverless web API utilizing API Gateway, Lambda, and DynamoDB", "Set up a highly resilient VPC network architecture"]
    },
    "Azure": {
        "duration": "4-6 Weeks",
        "courses": ["Microsoft Azure Fundamentals (AZ-900) Cert Prep (Udemy)", "AZ-104 Azure Administrator Prep (Coursera)"],
        "books": ["Microsoft Azure Architect Technologies study guides"],
        "projects": ["Deploy web applications on Azure App Service with Azure SQL", "Configure virtual networks and load balancers on Azure"]
    },
    "GCP": {
        "duration": "4-6 Weeks",
        "courses": ["Google Cloud Digital Leader (Coursera)", "GCP Associate Cloud Engineer (Udemy)"],
        "books": ["Official Google Cloud Certified Associate Cloud Engineer Study Guide"],
        "projects": ["Deploy a containerized application to Google Kubernetes Engine", "Set up big data pipelines using Pub/Sub, Dataflow, and BigQuery"]
    },
    "Docker": {
        "duration": "2 Weeks",
        "courses": ["Docker & Kubernetes: The Practical Guide (Udemy - Maximilian Schwarzmüller)", "Docker Technologies for Developers (Udemy)"],
        "books": ["Docker Deep Dive by Nigel Poulton"],
        "projects": ["Dockerize a multi-container full-stack app (React + Node + Postgres)", "Optimize Dockerfile builds utilizing multi-stage configurations"]
    },
    "Kubernetes": {
        "duration": "4-5 Weeks",
        "courses": ["Certified Kubernetes Administrator (CKA) with Practice Tests (Udemy - Mumshad Mannambeth)"],
        "books": ["Kubernetes up and Running by Kelsey Hightower"],
        "projects": ["Deploy a highly available app with rolling updates and ingress", "Configure horizontal pod autoscaling and persistent volume claims"]
    },
    # dev tools (NEW)
    "Git": {
        "duration": "1 Week",
        "courses": ["Git Complete: The Definitive Guide (Udemy)", "Version Control with Git (Coursera)"],
        "books": ["Pro Git by Scott Chacon"],
        "projects": ["Set up a local repository, practice branching, merging, and resolving conflicts", "Create a collaborative GitHub workflow with pull requests"]
    },
    "Linux": {
        "duration": "2 Weeks",
        "courses": ["Linux Command Line Basics (Udemy)", "Linux Foundation Certified System Administrator (LFCS) Prep"],
        "books": ["The Linux Command Line by William Shotts"],
        "projects": ["Write bash scripts to automate file backup and log rotation", "Configure server security configurations and environment paths"]
    },
    "Agile": {
        "duration": "1-2 Weeks",
        "courses": ["Agile with Atlassian Jira (Coursera)", "Scrum Master Certification Prep (Udemy)"],
        "books": ["User Stories Applied by Mike Cohn", "Scrum: The Art of Doing Twice the Work in Half the Time by Jeff Sutherland"],
        "projects": ["Create a Scrum/Kanban board for a software project with epics, sprints, and tasks", "Conduct mock daily stand-up and retrospective sessions"]
    },
    "REST_APIs": {
        "duration": "2 Weeks",
        "courses": ["REST API Design, Development & Management (Udemy)", "APIs and Web Services (Coursera)"],
        "books": ["RESTful Web APIs by Leonard Richardson"],
        "projects": ["Design a comprehensive REST API specification with Swagger/OpenAPI docs", "Build a backend CRUD API handling rate limiting and pagination"]
    },
    # soft skills
    "Communication": {
        "duration": "Ongoing",
        "courses": ["Communication Foundations (LinkedIn Learning)", "Speak with Confidence (Udemy)"],
        "books": ["Crucial Conversations by Joseph Grenny", "How to Win Friends and Influence People by Dale Carnegie"],
        "projects": ["Write a technical documentation guide for a complex system", "Present a 5-minute technical demo to peer groups"]
    },
    "Teamwork": {
        "duration": "Ongoing",
        "courses": ["Working in Teams (Coursera)", "Building Collaborative Teams (LinkedIn Learning)"],
        "books": ["The Five Dysfunctions of a Team by Patrick Lencioni"],
        "projects": ["Lead a collaborative project using Git/GitHub workflow", "Participate in or organize a 48-hour team hackathon"]
    },
    "Problem_Solving": {
        "duration": "Ongoing",
        "courses": ["Effective Problem-solving and Decision-making (Coursera)", "Creative Thinking & Problem Solving (edX)"],
        "books": ["Think Smarter: Critical Thinking to Solve Problems by Michael Kallet"],
        "projects": ["Optimize computational algorithms on LeetCode/HackerRank", "Conduct root cause analysis (RCA) on a past production failure"]
    },
    "Leadership": {
        "duration": "Ongoing",
        "courses": ["Leadership Foundation (LinkedIn Learning)", "Specialization in Leadership (Coursera - University of Michigan)"],
        "books": ["Start with Why by Simon Sinek", "Extreme Ownership by Jocko Willink"],
        "projects": ["Mentor a junior developer or classmate through a coding task", "Lead the planning and execution phase of a software milestone"]
    },
    "Presentation": {
        "duration": "1-2 Weeks",
        "courses": ["Presentation Skills: Public Speaking Bootcamp (Udemy)", "Designing Effective Slides (LinkedIn Learning)"],
        "books": ["Presentation Zen by Garr Reynolds"],
        "projects": ["Build and deliver a slideshow summarizing a data science project", "Create and record a video demo showcasing software features"]
    }
}
