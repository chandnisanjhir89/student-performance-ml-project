import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Student Data Explorer", layout="wide")

# Title and Description
st.title("🎓 Student Performance Dashboard")
st.write("This application allows you to explore student data and calculate average performance scores.")

# Data Loading
try:
    df = pd.read_csv('cleaned_students_data.csv')
    
    # Sidebar - Filters
    st.sidebar.header("Filter Options")
    gender_choice = st.sidebar.selectbox(
        "Select Gender", 
        options=[0, 1], 
        format_func=lambda x: "Male" if x == 1 else "Female"
    )
    
    # Main UI - Tabs
    tab1, tab2 = st.tabs(["📊 Data Preview", "📝 Score Calculator"])

    with tab1:
        st.subheader("Dataset Overview")
        # Display filtered data
        filtered_df = df[df['gender'] == gender_choice]
        # Updated 'width' parameter to avoid warning
        st.dataframe(filtered_df, width=1200) 
        
        # Basic Statistics
        st.subheader("Average Scores")
        col1, col2, col3 = st.columns(3)
        col1.metric("Avg Math Score", round(filtered_df['math score'].mean(), 2))
        col2.metric("Avg Reading Score", round(filtered_df['reading score'].mean(), 2))
        col3.metric("Avg Writing Score", round(filtered_df['writing score'].mean(), 2))

    with tab2:
        st.subheader("Enter Student Details")
        # Input fields
        col_a, col_b = st.columns(2)
        
        with col_a:
            parent_edu = st.selectbox("Parental Education Level", options=df['parental level of education'].unique())
            lunch_type = st.radio("Lunch Type (0: Standard, 1: Reduced)", options=[0, 1])
            test_prep = st.selectbox("Test Preparation Course (0: None, 1: Completed)", options=[0, 1])
            
        with col_b:
            m_score = st.slider("Math Score", 0, 100, 50)
            r_score = st.slider("Reading Score", 0, 100, 50)
            w_score = st.slider("Writing Score", 0, 100, 50)

        if st.button("Calculate Total Result"):
            total = m_score + r_score + w_score
            average = total / 3
            st.info(f"Total Marks: {total}/300 | Average Percentage: {average:.2f}%")

except FileNotFoundError:
    st.error("Error: 'cleaned_students_data.csv' file not found. Please ensure the file is in the correct directory.")