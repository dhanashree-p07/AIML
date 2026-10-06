import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI/ML Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f5f6f8;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e5e5;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #333333;
}

/* Main title */
.main-title {
    font-size: 36px;
    font-weight: 700;
    color: #222222;
    margin-bottom: 5px;
}

/* Subtitle */
.main-subtitle {
    color: #777777;
    font-size: 16px;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #e5e5e5;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* Card title */
.card-title {
    font-size: 20px;
    font-weight: 600;
    color: #222222;
    margin-bottom: 10px;
}

/* Small text */
.small-text {
    color: #777777;
    font-size: 14px;
}

/* Metric */
.metric-number {
    font-size: 30px;
    font-weight: bold;
    color: #222222;
}

.metric-label {
    color: #777777;
    font-size: 14px;
}

/* Prediction result */
.prediction {
    background-color: #f1f8f3;
    border: 1px solid #b7dfc1;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

.prediction-title {
    color: #267a3b;
    font-size: 18px;
    font-weight: bold;
}

.prediction-value {
    color: #1e6b32;
    font-size: 30px;
    font-weight: bold;
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    border: none;
    background-color: #333333;
    color: white;
    font-weight: 600;
    padding: 10px 20px;
}

.stButton > button:hover {
    background-color: #111111;
    color: white;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: white;
    border-radius: 10px;
}

/* Headers */
h1, h2, h3 {
    color: #222222;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown(
        """
        <h2 style="text-align:center;">
        🤖 AI/ML
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    menu = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🤖 Prediction",
            "📊 Data Analysis",
            "📁 Dataset",
            "🧠 Models",
            "👤 Profile",
            "⚙️ Settings"
        ]
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;color:#777;">
        <small>AI/ML Platform</small><br>
        <small>Version 1.0</small>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# DASHBOARD
# ==========================================

if menu == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">AI/ML Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Welcome to your Artificial Intelligence and Machine Learning platform.'
        '</div>',
        unsafe_allow_html=True
    )

    # Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="metric-number">12</div>
            <div class="metric-label">Models</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="metric-number">8</div>
            <div class="metric-label">Datasets</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="metric-number">94.6%</div>
            <div class="metric-label">Best Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="metric-number">248</div>
            <div class="metric-label">Predictions</div>
        </div>
        """, unsafe_allow_html=True)

    # Welcome card
    st.markdown("""
    <div class="card">
        <div class="card-title">🚀 AI/ML Workspace</div>
        <p class="small-text">
        Build, test and analyze Machine Learning models from one platform.
        Upload datasets, perform data analysis and generate predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick actions
    st.subheader("Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("🤖 Make Prediction", use_container_width=True):
            st.info("Go to Prediction from the sidebar.")

    with c2:
        if st.button("📁 Upload Dataset", use_container_width=True):
            st.info("Go to Dataset from the sidebar.")

    with c3:
        if st.button("📊 Analyze Data", use_container_width=True):
            st.info("Go to Data Analysis from the sidebar.")


# ==========================================
# PREDICTION
# ==========================================

elif menu == "🤖 Prediction":

    st.markdown(
        '<div class="main-title">🤖 AI Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Enter the required information and generate a prediction.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Input Data")

    col1, col2 = st.columns(2)

    with col1:

        feature1 = st.number_input(
            "Feature 1",
            value=5.0
        )

        feature2 = st.number_input(
            "Feature 2",
            value=3.0
        )

    with col2:

        feature3 = st.number_input(
            "Feature 3",
            value=4.0
        )

        feature4 = st.number_input(
            "Feature 4",
            value=2.0
        )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔮 Generate Prediction", use_container_width=True):

        # Demo prediction logic
        average = (
            feature1 +
            feature2 +
            feature3 +
            feature4
        ) / 4

        if average >= 4:
            result = "High"
        elif average >= 2:
            result = "Medium"
        else:
            result = "Low"

        st.markdown(
            f"""
            <div class="prediction">
                <div class="prediction-title">
                    Prediction Result
                </div>
                <div class="prediction-value">
                    {result}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# DATA ANALYSIS
# ==========================================

elif menu == "📊 Data Analysis":

    st.markdown(
        '<div class="main-title">📊 Data Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Explore your dataset using basic statistical analysis.'
        '</div>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully!")

        st.subheader("Dataset Preview")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader("Dataset Information")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Rows",
                df.shape[0]
            )

        with c2:
            st.metric(
                "Columns",
                df.shape[1]
            )

        with c3:
            st.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )

        st.subheader("Statistics")

        st.dataframe(
            df.describe(),
            use_container_width=True
        )

        # Numeric chart
        numeric_columns = df.select_dtypes(
            include=np.number
        ).columns

        if len(numeric_columns) > 0:

            st.subheader("Data Visualization")

            selected_column = st.selectbox(
                "Select column",
                numeric_columns
            )

            st.line_chart(
                df[selected_column]
            )

    else:

        st.info(
            "Upload a CSV dataset to start analyzing your data."
        )


# ==========================================
# DATASET
# ==========================================

elif menu == "📁 Dataset":

    st.markdown(
        '<div class="main-title">📁 Dataset Manager</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Upload and manage datasets for your ML projects.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a dataset",
        type=["csv", "xlsx"]
    )

    if uploaded_file:

        st.success(
            f"{uploaded_file.name} uploaded successfully!"
        )

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# MODELS
# ==========================================

elif menu == "🧠 Models":

    st.markdown(
        '<div class="main-title">🧠 ML Models</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Machine Learning models available in your workspace.'
        '</div>',
        unsafe_allow_html=True
    )

    models = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "K-Nearest Neighbors"
        ],
        "Type": [
            "Regression",
            "Classification",
            "Classification",
            "Classification",
            "Classification"
        ],
        "Status": [
            "Ready",
            "Ready",
            "Ready",
            "Ready",
            "Ready"
        ]
    })

    st.dataframe(
        models,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# PROFILE
# ==========================================

elif menu == "👤 Profile":

    st.markdown(
        '<div class="main-title">👤 Profile</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <div class="card-title">User Profile</div>
        <p><b>Name:</b> AI/ML Student</p>
        <p><b>Role:</b> Machine Learning Developer</p>
        <p><b>Projects:</b> 5</p>
        <p><b>Models:</b> 12</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Skills")

    st.progress(80)
    st.write("Python")

    st.progress(65)
    st.write("Machine Learning")

    st.progress(55)
    st.write("Deep Learning")

    st.progress(40)
    st.write("Generative AI")


# ==========================================
# SETTINGS
# ==========================================

elif menu == "⚙️ Settings":

    st.markdown(
        '<div class="main-title">⚙️ Settings</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Customize your AI/ML workspace.'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("Application Settings")

    dark_mode = st.toggle(
        "Dark Mode"
    )

    notifications = st.toggle(
        "Enable Notifications",
        value=True
    )

    auto_analysis = st.toggle(
        "Automatic Data Analysis",
        value=True
    )

    if st.button("Save Settings"):

        st.success(
            "Settings saved successfully!"
        )
