import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - Projects",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Projects ---
st.header("📂 Projects")
st.write("Below are some of the projects I have worked on in the past year (2024/25). ")
st.divider()
st.markdown("### 🥊Longitudinal Analysis of KO Rates in Amateur Boxing ")
st.write("This project involved analyzing the KO/Non-Finish rates in amateur boxing over time. " \
"Specifically looking at the impacts of rule changes and how they affected the KO rates in different weight classes and age groups.")
st.markdown("#### 3 main steps:")
st.markdown("##### 1. Cleaning of the dataset")
boxing_1 = [
    "Data was provided from BoxingGB but contained some errors and unstandardized formats",
    "Data was cleaned using Excel and PowerBI",
]
st.markdown("\n".join([f"- {skill}" for skill in boxing_1]))

st.write("")

st.markdown("##### 2. Exploratory Data Analysis via PowerBI")
boxing_2 = [
    "Visuals were created to identify trends in KO/Non-Finish rates amoungst different weight classes/Gender/Age groups",
    "The analysis was done using PowerBI",
]
st.markdown("\n".join([f"- {skill}" for skill in boxing_2]))

st.write("")

st.markdown("##### 3. Supplementing the exploratory analysis with additional longitudinal data")
boxing_3 = [
    "Longitudinal data was collected from the BoxingGB website and used to supplement the exploratory analysis",
    "Data was scraped using Python and BeautifulSoup",
    "Data was visualized in PowerBI to provide additional insights",
]
st.markdown("\n".join([f"- {skill}" for skill in boxing_3]))

st.write(" ")
with open("StreamLit Work Portfolio/assets/Longitudinal_boxing_KO_Analysis.pbix", "rb") as file:
    st.download_button(
        label="📄 Download Boxing Project",
        data=file,
        file_name="Longitudinal_boxing_KO_Analysis.pbix",
        mime="application/octet-stream"
    )
st.divider()
st.markdown("### 📊 Database Validation")
st.write("This project involved validating the AquaticsGB database, which consists of performance analysis data entered by various analysts over the last 2 decades. " \
"The goal was to ensure the accuracy and consistency of the data by cataloging and removing outliers that are then to be reveiwed. " \
"Additionally, profiling keeps track of where errors occur and who has made them.")
st.markdown("#### 3 main steps:")
st.markdown("##### 1. Generating Descriptive Statistics")
DF_1 = [
    " Data provided from AquaticsGB was cleaned and statistics were generated based on conditional race data (ex. distance, gender, stroke, ect.)",
    " A reduced dataset was used to generate descriptive statistics (approx. 35,000 rows & 900 columns)",
    " Descriptive statistics were generated using Python and Pandas",
    " Program was built with a user-friendly installable package using custom Tkinter GUI and Inno Setup Compiler so that it can easily be used by non-technical staff",
]
st.markdown("\n".join([f"- {skill}" for skill in DF_1]))

st.write(" ")

st.markdown("##### 2. Saving Outliers & Generating Error Reports")
DF_2 = [
    "Outliers were removed based on their z-scores generated from the descriptive statistics",
    "Outliers were added to a separate dataset for review",
    "Error reports were generated based on the outliers removed",
    "Program was built with a user-friendly installable package using custom Tkinter GUI and Inno Setup Compiler so that it can easily be used by non-technical staff",
]
st.markdown("\n".join([f"- {skill}" for skill in DF_2]))

st.write(" ")

st.markdown("##### 3. Profiling of Errors")
DF_3 = [
    "Using the error reports generated, a profiling of errors was created to identify where errors occur and who has made them",
    "Profiling was done using a custom Python script, although it can also be done using PowerBI or Tableau",
]
st.markdown("\n".join([f"- {skill}" for skill in DF_3]))

st.write(" ")
# This will need to be chnaged to the correct file path
with open("StreamLit Work Portfolio/assets/Database_Validation_Example.pdf", "rb") as file:
    st.download_button(
        label="📄 Download Aquatics Project Summary",
        data=file,
        file_name="Database_Validation_Example.pdf",
        mime="application/pdf"
    )

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("## Upcoming Projects")
st.divider()

st.markdown("### 📈 Predictive Analysis of Swimming Performance")
st.write("""
This project involves using multiple regression and machine learning to predict swimming performance based on historical data. 
Specifically, the goal was to predict the performance of swimmers in the 100m freestyle relay event based on recent meet data. 
However, the program was designed to be flexible enough to be used for any event as it is compatible with raw outputs from the AquaticsGB database. 
This project is not yet complete but is expected to be finished by August of 2025. The goal is to have a user-friendly program that can aid coaches and training staff in estimating certain metrics 
that are associated with elite performance, allowing coaches to manipulate the metrics of a theoretical race and estimate an expected finishing time.
""")
st.markdown("#### 3 main steps:")
st.markdown("##### 1. Collecting & Analyzing Data")
prediction_1 = [
    "Data will be collected and analysed from 2 international meets (2023 World Aquatic Championships and 2024 Olympic Games",
]
st.markdown("\n".join([f"- {skill}" for skill in prediction_1]))

st.write(" ")

st.markdown("##### 2. Building a Predictive Model")
prediction_2 = [
    "A predictive model will be built using Principle Componant Analysis, multiple regression, and machine learning techniques",
    "The program (currently in development) has a user-friendly interface and is designed to be flexible enough to be used for any event",
    "Statistical procedures are built using Python and Scikit-learn",
]
st.markdown("\n".join([f"- {skill}" for skill in prediction_2]))
st.write(" ")
st.markdown("##### 3. Comparing Results")
prediction_3 = [
    "The results of the predictive model will be compared to results of out of sample data (2025 World Aquatic Championships)",
]
st.markdown("\n".join([f"- {skill}" for skill in prediction_3]))

st.write(" ")

with open("StreamLit Work Portfolio/assets/Performance_Prediction_of_the_Mens_100m_Freestyle.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My Proposal",
        data=file,
        file_name="Performance_Prediction_Proposal.pdf",
        mime="application/pdf"
    )
st.divider()

st.markdown("### 🚴‍♂️ Analysis of Variables Influencing Variables in Track Cycling Start Performance")
st.write("""
This project, paired with GB Track Cycling, plans to analyze 4 years of data including 10 m, quarter lap, half lap splits timing, Power data (Peak,
average), cadence and speed. The goals is to provide insight in terms of the measured variables and performance times. 
         """)

st.write(" ")
st.divider()
st.markdown("### 🚴‍♂️ What is the optimal starting technique in track cycling?")
st.write("""
This project, paired with GB Track Cycling, plans to analyze the optimal starting technique in track cycling using crank data and 2D marker tracking to identify key determinates of performance.
The goal is to identify the optimal starting technique for track cycling and provide recommendations for coaches and athletes.
""")
