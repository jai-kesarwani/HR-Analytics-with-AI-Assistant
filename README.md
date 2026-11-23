# 📊 HR Analytics with AI Assistant

An end-to-end **HR Analytics project** that combines data analytics, interactive Power BI dashboards, SQL-based business analysis, and a Generative AI-powered assistant.

The project analyzes employee attrition, workforce demographics, salary patterns, overtime trends, promotion gaps, and retention risks. It also integrates the **Google Gemini API** to generate analytical summaries, key insights, business impact, and actionable recommendations from HR analytics results.

By combining traditional data analytics with AI-generated explanations, this project aims to make workforce data easier to understand and support data-driven HR decision-making.

---

## 🎯 Project Objectives

- Analyze workforce demographics and employee distribution.
- Identify factors associated with employee attrition.
- Study compensation, overtime, promotion gaps, and job satisfaction.
- Identify employee groups and departments with elevated retention risk.
- Build interactive Power BI dashboards for workforce analysis.
- Generate AI-powered summaries and key insights using Gemini.
- Explain the potential business impact of analytical findings.
- Provide actionable recommendations to support employee retention.

---

## 🤖 AI Assistant — Gemini API

The project includes a Python-based AI Assistant located in the `HR_Assistant` directory. It uses Google's **Gemini API as the Large Language Model (LLM)** to transform HR analytics findings into understandable business insights.

### Key Features

- **📋 Summary:** Generates a concise overview of the HR analytics results.
- **🔍 Key Insights:** Highlights important workforce patterns and attrition trends.
- **📈 Business Impact:** Explains the potential implications of the findings for employee retention, productivity, and workforce planning.
- **💡 Recommendations:** Suggests possible strategies to improve employee satisfaction and reduce attrition.
- **🧠 LLM Integration:** Uses Gemini to generate natural-language responses based on the analytical context provided to the assistant.

### How It Works

1. HR data is cleaned and analyzed using Python and SQL.
2. Analytical findings are explored through Power BI dashboards.
3. Relevant analytical information is supplied to the AI assistant.
4. The Gemini API processes the provided context.
5. The assistant generates a summary, key insights, business impact, and recommendations.

The assistant complements data analysis by helping users interpret results and communicate findings in a business-friendly format.

---

## 🛠️ Tools & Technologies

| Technology | Purpose |
|---|---|
| Excel | Initial data cleaning and exploration |
| Python | Data preprocessing, feature engineering, and exploratory analysis |
| Pandas & NumPy | Data manipulation and numerical analysis |
| Matplotlib & Seaborn | Data visualization and exploratory analysis |
| PostgreSQL | SQL queries and workforce analysis |
| Power BI | Interactive dashboards and business reporting |
| Google Gemini API | AI-generated summaries, insights, business impact, and recommendations |
| Git & GitHub | Version control and project documentation |

---

## 📂 Project Workflow

```text
HR Analytics Dataset
        ↓
Excel Data Cleaning
        ↓
Python EDA & Feature Engineering
        ↓
PostgreSQL Business Analysis
        ↓
Power BI Dashboards
        ↓
Analytical Findings
        ↓
Python AI Assistant
        ↓
Google Gemini API
        ↓
Summary • Key Insights
Business Impact • Recommendations
```

---

## 📌 Dataset

**Dataset:** IBM HR Analytics Employee Attrition Dataset

The dataset contains employee information related to:

- Employee demographics
- Department and job role
- Salary and income
- Overtime
- Job satisfaction
- Employee experience and tenure
- Promotion-related analysis
- Performance indicators
- Attrition status

The dataset is used to explore workforce trends and identify factors associated with employee turnover.

---

## 🧹 Data Cleaning & Feature Engineering

Data preparation and feature engineering include:

- Checking missing values and duplicate records.
- Removing irrelevant columns where appropriate.
- Preparing data for exploratory analysis and visualization.
- Creating additional analytical features:
  - `PromotionGap`
  - `AnnualIncome`
  - `AgeGroup`
  - `Risk Category`
- Preparing cleaned data for SQL analysis and Power BI.

---

## 🗄️ SQL Business Analysis

PostgreSQL is used to analyze workforce trends and answer important HR business questions.

Examples include:

- What is the overall employee attrition rate?
- Which departments experience the highest attrition?
- How is overtime associated with employee attrition?
- Which job roles have higher turnover?
- Is a longer promotion gap associated with employee attrition?
- Which employees fall into high-risk categories?
- Which departments have the most high-risk employees?
- How does salary vary across job roles?
- How do attrition patterns differ across employee groups?

The resulting analysis supports dashboard development and provides useful context for AI-generated explanations.

---

## 📈 Python Exploratory Data Analysis

Python is used to explore employee data, identify patterns, and prepare analytical findings.

### Analysis Areas

- Workforce distribution
- Employee attrition trends
- Salary distribution
- Promotion gap analysis
- Overtime versus attrition
- Job satisfaction analysis
- Age-group segmentation
- Workforce risk analysis

### Libraries

```python
pandas
numpy
matplotlib
seaborn
```

---

## 📊 Power BI Dashboard

The Power BI report contains three major analytical sections.

### 1️⃣ Workforce Overview

- Total employees
- Attrition rate
- Average salary
- Average age
- Department distribution
- Gender distribution
- Age-group analysis

### 2️⃣ Employee Attrition Analysis

- Department-wise attrition
- Job role attrition
- Overtime versus attrition
- Salary versus attrition
- Promotion gap analysis
- Job satisfaction analysis

### 3️⃣ Workforce Risk Analysis & Recommendations

- Risk category distribution
- Department-wise workforce risk
- High-risk employee analysis
- Potential retention risk factors
- Strategic recommendations

---

## 📷 Dashboard Screenshots

### Workforce Overview

![Workforce Overview](Screenshots/dashboard/Workforce%20Overview.png)

### Employee Attrition Analysis

![Employee Attrition Analysis](Screenshots/dashboard/Employee%20Attrition.png)

### Workforce Risk Analysis

![Workforce Risk Analysis](Screenshots/dashboard/Risk%20Analysis%20%26%20Recommendation.png)

---

## 🗄️ SQL Analysis Screenshots

### Attrition Rate

![Attrition Rate](Screenshots/sql%20insights/Attrition%20Rate.png)

### Department-wise Attrition

![Department-wise Attrition](Screenshots/sql%20insights/Dept-wise%20attrition.png)

### Job Role Ranking by Average Salary

![Job Role Salary Ranking](Screenshots/sql%20insights/job%20role%20rank.png)

### High-Risk Employee Analysis

![High-Risk Employee Analysis](Screenshots/sql%20insights/high%20risk%20employee.png)

### Risk Category Analysis

![Risk Category Analysis](Screenshots/sql%20insights/risk%20category.png)

### Salary Analysis

![Salary Analysis](Screenshots/sql%20insights/salary%20analysis.png)

---

## 🧠 AI Assistant Integration

The AI assistant uses the Gemini API to explain analytical findings in a clear and structured format.

| Output | Description |
|---|---|
| Summary | Provides an overview of the analytical findings |
| Key Insights | Highlights important trends and patterns |
| Business Impact | Explains the potential organizational implications |
| Recommendations | Suggests possible actions based on the findings |

### Example Use Case

If the analysis identifies a higher attrition rate among employees working overtime, the assistant can explain the finding, discuss its potential implications for work-life balance and retention, and suggest reviewing overtime practices.

AI-generated outputs depend on the data and context supplied to the model. Recommendations should be validated against the underlying analysis before making business decisions.

---

## 💡 Key Findings & Business Recommendations

The analysis explores several potential workforce patterns:

1. Employees working overtime may exhibit higher attrition rates.
2. Longer promotion gaps and lower job satisfaction may be associated with increased retention risk.
3. Attrition and workforce risk may vary across departments and job roles.
4. Salary differences may be associated with employee turnover patterns.
5. Attrition trends may differ across age groups.

### Recommended Actions

- Improve career development and promotion transparency.
- Review overtime practices and workload distribution.
- Strengthen employee engagement initiatives.
- Investigate departments with elevated attrition.
- Review compensation patterns across roles and experience levels.
- Use AI-generated summaries to communicate analytical findings to stakeholders.

These patterns indicate associations rather than proof of causation. Recommendations should be evaluated using organizational context and additional evidence.

---

## 📁 Project Structure

```text
HR_ANALYTICS/
│
├── Dataset/
│   ├── HR_Analytics.csv
│   └── HR_Cleaned.csv
│
├── HR_Assistant/
│   ├── main.py
│   ├── pyproject.toml
│   ├── uv.lock
│
├── Screenshots/
│   ├── dashboard/
│   │   ├── Employee Attrition.png
│   │   ├── Risk Analysis & Recommendation.png
│   │   └── Workforce Overview.png
│   │
│   └── sql insights/
│       ├── Attrition Rate.png
│       ├── Dept-wise attrition.png
│       ├── high risk employee.png
│       ├── job role rank.png
│       ├── risk category.png
│       └── salary analysis.png
│
├── .gitignore
├── HR_Analytics Dashboard.pbix
├── HR_Analytics_SQL_Queries.sql
└── HR_Analytics.ipynb
```

*Environment folders and secret configuration files are intentionally excluded from this project tree.*

---

## ⚙️ Running the AI Assistant

### Prerequisites

- Python installed on your system
- A Gemini API key
- Required Python dependencies for the assistant

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd HR_ANALYTICS
```

### 2. Navigate to the AI Assistant

```bash
cd HR_Assistant
```

### 3. Install Dependencies

If the project uses `uv`, install it first and then run:

```bash
uv sync
```

This installs the dependencies declared in `pyproject.toml` and managed through `uv.lock`.

### 4. Configure the Gemini API Key

Create a local `.env` file inside `HR_Assistant` and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual API key. Never commit `.env` files or API credentials to GitHub.

### 5. Run the Application

```bash
uv run python main.py
```

The exact environment variable name, dependency configuration, and launch command should match the implementation in `main.py` and `pyproject.toml`.

---

## 🚀 Future Improvements

- Develop an employee attrition prediction model.
- Add conversational questions and answers for HR analytics.
- Connect AI-generated explanations more closely with Power BI insights.
- Deploy the assistant as a web application.
- Introduce advanced workforce segmentation.
- Automate periodic HR reporting.
- Improve AI response validation and traceability.

---

## 👤 Author

**Jai Kesarwani**

Aspiring Data Analyst | Python | SQL | Power BI | Data Visualization | Generative AI

---

⭐ If you find this project useful, consider giving the repository a star!
