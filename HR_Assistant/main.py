import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
import os


st.set_page_config(
    page_title="AI HR Analytics Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI HR Analytics Assistant")
st.caption("AI Powered HR Dashboard | SQL | Python | Gemini")

# loading api key

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# loading dataset

@st.cache_data
def load_data():
    df = pd.read_csv("../Dataset/HR_Cleaned.csv")
    return df

df = load_data()

# session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "report" not in st.session_state:
    st.session_state.report = ""

# Previewing dataset
with st.expander("Preview Dataset"):

    st.dataframe(df.head())

# dashboard metrics
employees = len(df)

departments = df["Department"].nunique()

attrition_rate = (
    (df["Attrition"]=="Yes").mean()*100
)

average_salary = df["MonthlyIncome"].mean()

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "Employees",
        employees
    )

with c2:

    st.metric(
        "Departments",
        departments
    )

with c3:

    st.metric(
        "Attrition Rate",
        f"{attrition_rate:.2f}%"
    )

with c4:

    st.metric(
        "Avg Salary",
        f"₹{average_salary:,.0f}"
    )


# HR analytics function

# highest attrition
def highest_attrition():

    result = (
        df.groupby("Department")["Attrition"]
        .apply(lambda x:(x=="Yes").mean()*100)
    )

    department = result.idxmax()

    rate = result.max()

    return department,rate

# Avg dept salary
def get_average_salary():

    return round(df["MonthlyIncome"].mean(),2)

# Highest dept salary
def highest_salary_department():

    result = (
        df.groupby("Department")["MonthlyIncome"]
        .mean()
    )

    dept = result.idxmax()

    salary = result.max()

    return dept,salary

# Lowest dept salary
def lowest_salary_department():

    result = (
        df.groupby("Department")["MonthlyIncome"]
        .mean()
    )

    dept = result.idxmin()

    salary = result.min()

    return dept,salary


# Gender
def get_gender_distribution():

    male = len(df[df["Gender"]=="Male"])

    female = len(df[df["Gender"]=="Female"])

    return male,female

# Overtime
def get_overtime():

    yes = len(df[df["OverTime"]=="Yes"])

    no = len(df[df["OverTime"]=="No"])

    return yes,no

# Job satisfaction
def get_satisfaction():

    return round(df["JobSatisfaction"].mean(),2)

# Performance
def get_performance():

    return round(df["PerformanceRating"].mean(),2)

# Streamlit Chat UI
st.divider()

st.subheader("🤖 HR AI Assistant")

st.write("### Suggested Questions")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.info("Highest Attrition")

with c2:

    st.info("Average Salary")

with c3:

    st.info("Gender Distribution")

with c4:

    st.info("Overtime Analysis")



for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

question = st.chat_input(
    "Ask anything about HR..."
)

# AI function
def ask_gemini(prompt):

    response = model.generate_content(prompt)

    return response.text

# Chatbot Response
if question:

    st.session_state.messages.append(
    {
        "role":"user",
        "content":question
    }
    )

    q = question.lower()

    prompt = ""

    if "highest attrition" in q:

        dept,rate = highest_attrition()

        prompt=f"""
Department : {dept}

Attrition Rate : {rate:.2f}%

Explain this.

Give recommendations.
"""

    elif "average salary" in q:

        salary=get_average_salary()

        prompt=f"""
Average Monthly Salary

₹{salary}

Explain what this means.

Give HR recommendations.
"""

    elif "highest salary" in q:

        dept,salary=highest_salary_department()

        prompt=f"""
Highest Salary Department

{dept}

Average Salary

₹{salary:.0f}

Explain.

Give recommendations.
"""

    elif "lowest salary" in q:

        dept,salary=lowest_salary_department()

        prompt=f"""
Lowest Salary Department

{dept}

Average Salary

₹{salary:.0f}

Explain.

Give recommendations.
"""

    elif "gender" in q:

        male,female=get_gender_distribution()

        prompt=f"""
Male Employees

{male}

Female Employees

{female}

Analyse gender diversity.

Recommend improvements.
"""

    elif "overtime" in q:

        yes,no=get_overtime()

        prompt=f"""
Employees Working Overtime

Yes={yes}

No={no}

Explain.

Give HR recommendations.
"""

    elif "performance" in q:

        performance=get_performance()

        prompt=f"""
Average Performance Rating

{performance}

Explain.

Recommend improvements.
"""

    elif "satisfaction" in q:

        sat=get_satisfaction()

        prompt=f"""
Average Job Satisfaction

{sat}

Explain.

Recommend improvements.
"""

    else:

        prompt=f"""
You are an HR Analytics Assistant.

Answer this question professionally.

Question:

{question}

If numerical information is unavailable, clearly say so.
"""

    with st.spinner("HR AI is thinking..."):
        final_prompt=f"""
You are an experienced HR Analytics Consultant.

Your audience is HR Managers and CEOs.

Always answer in this format.

## Summary

## Key Insights

## Business Impact

## Recommendations

Keep the answer professional.

Analytics

{prompt}
"""
        answer=ask_gemini(final_prompt)

    st.session_state.messages.append(
    {
        "role":"user",
        "content":question
    }
    )


# loading dashboard metrics 
def get_dashboard_metrics():

    employees = len(df)

    department, rate = highest_attrition()

    salary = get_average_salary()

    performance = get_performance()

    satisfaction = get_satisfaction()

    male, female = get_gender_distribution()

    overtime_yes, overtime_no = get_overtime()

    return {
        "employees": employees,
        "department": department,
        "rate": rate,
        "salary": salary,
        "performance": performance,
        "satisfaction": satisfaction,
        "male": male,
        "female": female,
        "overtime_yes": overtime_yes,
        "overtime_no": overtime_no
    }

# AI recommendation code

st.divider()

st.subheader("💡 AI Recommendations")

if st.button("Generate AI HR Insights"):

    data = get_dashboard_metrics()

    prompt = f"""
You are an HR Analytics Consultant.

Analyze the HR dashboard below and provide business recommendations.

HR Dashboard

Total Employees: {data['employees']}

Highest Attrition Department: {data['department']}

Attrition Rate: {data['rate']:.2f}%

Average Monthly Salary: ₹{data['salary']:.2f}

Average Job Satisfaction: {data['satisfaction']}

Average Performance Rating: {data['performance']}

Male Employees: {data['male']}

Female Employees: {data['female']}

Employees Working Overtime: {data['overtime_yes']}

Employees Not Working Overtime: {data['overtime_no']}

Generate:

1. Executive Summary

2. Key Findings

3. Top 5 HR Recommendations

4. Future Action Plan

Use bullet points.
"""

    with st.spinner("Generating AI Recommendations..."):

        recommendations = ask_gemini(prompt)

    st.success("Recommendations Generated")

    st.markdown(recommendations)

# Executive reports

st.divider()

st.subheader("📄 Executive HR Report")

if st.button("Generate Executive Report"):

    data = get_dashboard_metrics()

    report_prompt = f"""
You are the Chief HR Officer of a company.

Write a professional HR Executive Report.

Use the following sections:

# Executive Summary

# Workforce Overview

# Attrition Analysis

# Salary Analysis

# Performance Analysis

# Employee Satisfaction

# Business Impact

# HR Recommendations

# Future Strategy

HR Dashboard Data

Total Employees: {data['employees']}

Highest Attrition Department: {data['department']}

Attrition Rate: {data['rate']:.2f}%

Average Salary: ₹{data['salary']:.2f}

Average Job Satisfaction: {data['satisfaction']}

Average Performance Rating: {data['performance']}

Male Employees: {data['male']}

Female Employees: {data['female']}

Employees Working Overtime: {data['overtime_yes']}

Employees Not Working Overtime: {data['overtime_no']}

Write the report professionally.
"""

    with st.spinner("Generating Executive Report..."):

        report = ask_gemini(report_prompt)

    st.session_state.report = report

    st.success("Executive Report Generated")

    st.markdown(report)

# Download report
if st.session_state.report:

    st.download_button(
        label="📥 Download Executive Report",
        data=st.session_state.report,
        file_name="Executive_HR_Report.txt",
        mime="text/plain"
    )

# AI insight card
st.info("""
💡 AI Insight

Employees working overtime are often associated with lower job satisfaction and higher attrition.

Use the AI Assistant below for deeper recommendations.
""")
