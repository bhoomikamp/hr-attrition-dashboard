# 👥 HR Analytics — Employee Attrition Dashboard

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458?logo=pandas)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?logo=tableau)
![SQL](https://img.shields.io/badge/SQL-12%20Queries-4479A1?logo=mysql)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

An end-to-end HR Analytics project analyzing **1,470 employee records** (IBM HR Analytics style dataset) to uncover attrition drivers, identify high-risk segments, and build an interactive **Tableau dashboard** for HR decision-makers.

---

## 📌 Project Objective

- Identify which **departments, roles, and demographics** have the highest attrition
- Understand the impact of **overtime, salary, satisfaction scores, and tenure** on attrition
- Segment employees into **risk categories** based on behavioral and demographic factors
- Build a multi-page **Tableau dashboard** to visualize KPIs and enable drill-down analysis
- Provide **actionable retention recommendations** backed by data

---

## 🗂️ Project Structure

```
hr-attrition-dashboard/
│
├── data/
│   └── hr_attrition.csv               # Dataset (1,470 employees, 28 features)
│
├── scripts/
│   ├── eda_analysis.py                # EDA + 10 visualization charts
│   └── sql_queries.sql                # 12 HR business SQL queries
│
├── notebooks/
│   └── HR_Attrition_Notebook.ipynb    # Complete Jupyter walkthrough
│
├── tableau/
│   └── TABLEAU_GUIDE.md               # Step-by-step Tableau dashboard guide
│
├── assets/
│   ├── 01_attrition_overview.png
│   ├── 02_attrition_by_department.png
│   ├── 03_attrition_by_jobrole.png
│   ├── 04_age_analysis.png
│   ├── 05_income_analysis.png
│   ├── 06_satisfaction_scores.png
│   ├── 07_overtime_travel.png
│   ├── 08_tenure_analysis.png
│   ├── 09_correlation_heatmap.png
│   └── 10_demographics.png
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Description

**File:** `data/hr_attrition.csv`
**Rows:** 1,470 employees | **Features:** 28 columns

| Column | Description |
|--------|-------------|
| `Age` | Employee age (18–60) |
| `Department` | Sales / Research & Development / Human Resources |
| `JobRole` | Specific job title (9 roles) |
| `MonthlyIncome` | Monthly salary in ₹ |
| `YearsAtCompany` | Tenure at the company |
| `JobSatisfaction` | 1 (Low) → 4 (Very High) |
| `WorkLifeBalance` | 1 (Bad) → 4 (Best) |
| `OverTime` | Yes / No |
| `BusinessTravel` | Non-Travel / Travel_Rarely / Travel_Frequently |
| `MaritalStatus` | Single / Married / Divorced |
| `Attrition` | **Target — Yes (Left) / No (Stayed)** |

---

## 📈 Key KPIs

| KPI | Value |
|-----|-------|
| 👥 Total Employees | 1,470 |
| 📉 Overall Attrition Rate | 30.0% |
| 🔴 Employees Left | 441 |
| 💰 Avg Income (Left) | ₹14,319 |
| 💰 Avg Income (Stayed) | ₹15,848 |
| ⏱️ Avg Age (Left) | 38.6 years |
| ⚠️ Attrition w/ Overtime | 39.1% |
| ✅ Attrition w/o Overtime | 20.4% |

---

## 🔍 Attrition by Department

| Department | Attrition Rate |
|-----------|----------------|
| Sales | 34.7% 🔴 |
| Research & Development | 28.4% 🟠 |
| Human Resources | 27.3% 🟡 |

---

## 💡 Key Business Insights

| # | Insight | Recommendation |
|---|---------|----------------|
| 1 | Sales has the highest attrition (34.7%) | Review compensation & incentive structure |
| 2 | Overtime employees churn at 39.1% vs 20.4% | Cap mandatory overtime; hire support staff |
| 3 | Low job satisfaction (score 1) = highest churn | Quarterly engagement surveys + action plans |
| 4 | First 3 years at company = highest risk window | Structured onboarding & mentorship programs |
| 5 | Single employees churn significantly more | Flexible work & social engagement initiatives |
| 6 | Frequent business travelers churn more | Limit travel frequency; offer travel perks |
| 7 | Low-income band has highest attrition | Benchmark and revise salary bands |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/hr-attrition-dashboard.git
cd hr-attrition-dashboard

# Install dependencies
pip install -r requirements.txt

# Run EDA (generates 10 charts)
python scripts/eda_analysis.py

# Open Jupyter Notebook
jupyter notebook notebooks/HR_Attrition_Notebook.ipynb
```

**For the Tableau dashboard**, follow the detailed guide in `tableau/TABLEAU_GUIDE.md`.

---

## 📉 Charts Generated (Python)

| # | Chart | Key Insight |
|---|-------|-------------|
| 1 | Overall Attrition Overview | 30% attrition rate |
| 2 | Attrition by Department | Sales is highest (34.7%) |
| 3 | Attrition by Job Role | Sales Rep & Lab Tech most at risk |
| 4 | Age Group Analysis | 18-25 have highest attrition |
| 5 | Income Boxplot | Left employees earn less |
| 6 | Satisfaction Scores | Lower satisfaction → higher attrition |
| 7 | Overtime & Travel | Overtime doubles attrition risk |
| 8 | Tenure Analysis | Early years = highest risk |
| 9 | Correlation Heatmap | Income & Tenure negatively correlated with attrition |
| 10 | Demographics | Single employees churn most |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.10+ | EDA & visualization |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | Chart generation (10 charts) |
| SQL (MySQL) | 12 business HR queries |
| Tableau (Public) | Interactive multi-page dashboard |
| Jupyter Notebook | Step-by-step analysis |
| Git & GitHub | Version control |

---

## 👨‍💻 Author

**Rahul Sharma**
B.Tech Computer Science | Data Analytics (Datamites)
📧 rahulsharma@email.com
🔗 [LinkedIn](https://linkedin.com/in/rahulsharma) | [GitHub](https://github.com/rahulsharma)

---

## 📄 License

Open-source under the [MIT License](LICENSE).
