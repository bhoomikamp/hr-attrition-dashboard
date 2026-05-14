-- ============================================================
-- HR Analytics — Employee Attrition SQL Queries
-- Author  : Rahul Sharma
-- DB      : MySQL / PostgreSQL compatible
-- Table   : hr_attrition
-- ============================================================

-- ─────────────────────────────────────────────
-- SETUP: Create Table
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS hr_attrition (
    EmployeeNumber           INT PRIMARY KEY,
    Age                      INT,
    Gender                   VARCHAR(10),
    MaritalStatus            VARCHAR(15),
    Department               VARCHAR(40),
    JobRole                  VARCHAR(40),
    EducationField           VARCHAR(30),
    Education                INT,
    JobLevel                 INT,
    MonthlyIncome            INT,
    PercentSalaryHike        INT,
    StockOptionLevel         INT,
    PerformanceRating        INT,
    JobSatisfaction          INT,
    EnvironmentSatisfaction  INT,
    WorkLifeBalance          INT,
    JobInvolvement           INT,
    BusinessTravel           VARCHAR(25),
    OverTime                 VARCHAR(5),
    TotalWorkingYears        INT,
    YearsAtCompany           INT,
    YearsInCurrentRole       INT,
    YearsSinceLastPromotion  INT,
    NumCompaniesWorked       INT,
    TrainingTimesLastYear    INT,
    DistanceFromHome         INT,
    Attrition                VARCHAR(5)
);


-- ─────────────────────────────────────────────
-- Q1: Overall Attrition Summary
-- ─────────────────────────────────────────────
SELECT
    Attrition,
    COUNT(*)                                            AS employee_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2)  AS percentage,
    ROUND(AVG(MonthlyIncome), 0)                        AS avg_monthly_income,
    ROUND(AVG(Age), 1)                                  AS avg_age,
    ROUND(AVG(YearsAtCompany), 1)                       AS avg_tenure_years
FROM hr_attrition
GROUP BY Attrition;


-- ─────────────────────────────────────────────
-- Q2: Attrition Rate by Department
-- ─────────────────────────────────────────────
SELECT
    Department,
    COUNT(*)                                                              AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)                   AS employees_left,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct,
    ROUND(AVG(MonthlyIncome), 0)                                          AS avg_income
FROM hr_attrition
GROUP BY Department
ORDER BY attrition_rate_pct DESC;


-- ─────────────────────────────────────────────
-- Q3: Attrition Rate by Job Role
-- ─────────────────────────────────────────────
SELECT
    JobRole,
    Department,
    COUNT(*)                                                              AS total,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)                   AS left_count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct,
    ROUND(AVG(MonthlyIncome), 0)                                          AS avg_income
FROM hr_attrition
GROUP BY JobRole, Department
ORDER BY attrition_rate_pct DESC;


-- ─────────────────────────────────────────────
-- Q4: Impact of Overtime on Attrition
-- ─────────────────────────────────────────────
SELECT
    OverTime,
    COUNT(*)                                                              AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)                   AS employees_left,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct
FROM hr_attrition
GROUP BY OverTime;


-- ─────────────────────────────────────────────
-- Q5: Attrition by Age Group
-- ─────────────────────────────────────────────
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        ELSE '46-60'
    END AS age_group,
    COUNT(*)                                                              AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)                   AS employees_left,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct
FROM hr_attrition
GROUP BY age_group
ORDER BY attrition_rate_pct DESC;


-- ─────────────────────────────────────────────
-- Q6: Salary Band vs Attrition
-- ─────────────────────────────────────────────
SELECT
    CASE
        WHEN MonthlyIncome < 5000  THEN 'Low (<5K)'
        WHEN MonthlyIncome < 10000 THEN 'Mid (5K-10K)'
        WHEN MonthlyIncome < 20000 THEN 'High (10K-20K)'
        ELSE 'Very High (>20K)'
    END AS salary_band,
    COUNT(*)                                                              AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)                   AS employees_left,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct
FROM hr_attrition
GROUP BY salary_band
ORDER BY attrition_rate_pct DESC;


-- ─────────────────────────────────────────────
-- Q7: Satisfaction Scores vs Attrition
-- ─────────────────────────────────────────────
SELECT
    JobSatisfaction,
    COUNT(*)                                                              AS total,
    ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct,
    ROUND(AVG(MonthlyIncome), 0)                                          AS avg_income
FROM hr_attrition
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;


-- ─────────────────────────────────────────────
-- Q8: Business Travel vs Attrition
-- ─────────────────────────────────────────────
SELECT
    BusinessTravel,
    COUNT(*)                                                              AS total,
    ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct
FROM hr_attrition
GROUP BY BusinessTravel
ORDER BY attrition_rate_pct DESC;


-- ─────────────────────────────────────────────
-- Q9: Marital Status vs Attrition
-- ─────────────────────────────────────────────
SELECT
    MaritalStatus,
    COUNT(*)                                                              AS total,
    ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct,
    ROUND(AVG(MonthlyIncome), 0)                                          AS avg_income
FROM hr_attrition
GROUP BY MaritalStatus
ORDER BY attrition_rate_pct DESC;


-- ─────────────────────────────────────────────
-- Q10: High Risk Employees
--      (Low satisfaction + OverTime + Low income)
-- ─────────────────────────────────────────────
SELECT
    EmployeeNumber, Department, JobRole, Age,
    MonthlyIncome, JobSatisfaction, WorkLifeBalance,
    OverTime, BusinessTravel, YearsAtCompany, Attrition
FROM hr_attrition
WHERE JobSatisfaction <= 2
  AND OverTime = 'Yes'
  AND MonthlyIncome < 5000
ORDER BY MonthlyIncome ASC;


-- ─────────────────────────────────────────────
-- Q11: Tenure Bucket Analysis
-- ─────────────────────────────────────────────
SELECT
    CASE
        WHEN YearsAtCompany < 2   THEN '0-1 years'
        WHEN YearsAtCompany < 5   THEN '2-4 years'
        WHEN YearsAtCompany < 10  THEN '5-9 years'
        ELSE '10+ years'
    END AS tenure_bucket,
    COUNT(*)                                                              AS total,
    ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct
FROM hr_attrition
GROUP BY tenure_bucket
ORDER BY attrition_rate_pct DESC;


-- ─────────────────────────────────────────────
-- Q12: Department × OverTime Attrition Matrix
-- ─────────────────────────────────────────────
SELECT
    Department,
    OverTime,
    COUNT(*)                                                              AS total,
    ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0
          / COUNT(*), 2)                                                  AS attrition_rate_pct
FROM hr_attrition
GROUP BY Department, OverTime
ORDER BY Department, attrition_rate_pct DESC;
