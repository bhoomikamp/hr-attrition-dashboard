"""
eda_analysis.py
===============
HR Analytics — Employee Attrition EDA & Visualization
Author  : Rahul Sharma
Tools   : Python (Pandas, NumPy, Matplotlib, Seaborn)
Dataset : data/hr_attrition.csv  (1,470 employees, 28 features)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings, os

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({"figure.dpi": 130, "font.family": "DejaVu Sans"})

BLUE   = "#1F4E79"
RED    = "#C73E1D"
GREEN  = "#2E7D32"
ORANGE = "#F18F01"
PURPLE = "#6A0572"
PALETTE = {"Yes": RED, "No": "#2E86AB"}

BASE   = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "../assets")
DATA   = os.path.join(BASE, "../data/hr_attrition.csv")
os.makedirs(ASSETS, exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════════
# 1. LOAD & OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════
df = pd.read_csv(DATA)
df["Attrition_Flag"] = (df["Attrition"] == "Yes").astype(int)

attr_rate = df["Attrition_Flag"].mean() * 100
total     = len(df)
left      = df["Attrition_Flag"].sum()
stayed    = total - left

print("=" * 60)
print("  HR ATTRITION ANALYSIS — DATA OVERVIEW")
print("=" * 60)
print(f"  Total Employees   : {total:,}")
print(f"  Attrition Rate    : {attr_rate:.1f}%")
print(f"  Employees Left    : {left:,}")
print(f"  Employees Stayed  : {stayed:,}")
print(f"  Columns           : {df.shape[1]}")
print(f"  Null Values       : {df.isnull().sum().sum()}")

# ═══════════════════════════════════════════════════════════════════════════
# 2. OVERALL ATTRITION DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════════
counts = df["Attrition"].value_counts()
fig, axes = plt.subplots(1, 2, figsize=(11, 5))
fig.suptitle("Overall Attrition Distribution", fontsize=14, fontweight="bold", color=BLUE)

axes[0].bar(["Stayed", "Left"], [stayed, left],
            color=["#2E86AB", RED], width=0.4, edgecolor="white")
axes[0].set_title("Employee Count"); axes[0].set_ylabel("Number of Employees")
for i, (v, lbl) in enumerate(zip([stayed, left], [stayed, left])):
    axes[0].text(i, v + 10, f"{v:,}\n({v/total*100:.1f}%)", ha="center", fontsize=11)

axes[1].pie([stayed, left], labels=["Stayed", "Left"],
            autopct="%1.1f%%", colors=["#2E86AB", RED],
            startangle=90, wedgeprops={"edgecolor": "white", "linewidth": 2})
axes[1].set_title("Attrition Rate")
plt.tight_layout()
plt.savefig(f"{ASSETS}/01_attrition_overview.png", bbox_inches="tight")
plt.close()
print("\n  [Saved] 01_attrition_overview.png")

# ═══════════════════════════════════════════════════════════════════════════
# 3. ATTRITION BY DEPARTMENT
# ═══════════════════════════════════════════════════════════════════════════
dept = df.groupby("Department").agg(
    total=("Attrition_Flag", "count"),
    left=("Attrition_Flag", "sum")
).reset_index()
dept["rate"] = dept["left"] / dept["total"] * 100
dept = dept.sort_values("rate", ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Attrition by Department", fontsize=14, fontweight="bold", color=BLUE)

axes[0].bar(dept["Department"], dept["rate"],
            color=[RED, ORANGE, "#2E86AB"], width=0.5, edgecolor="white")
axes[0].set_title("Attrition Rate (%)"); axes[0].set_ylabel("Attrition Rate (%)")
axes[0].axhline(attr_rate, color="gray", linestyle="--", linewidth=1.5,
                label=f"Overall ({attr_rate:.1f}%)")
axes[0].legend()
for i, v in enumerate(dept["rate"]):
    axes[0].text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=11, fontweight="bold")

axes[1].bar(dept["Department"], dept["total"], label="Total", color="#D6E4F0",
            edgecolor="#1F4E79", width=0.5)
axes[1].bar(dept["Department"], dept["left"], label="Left", color=RED,
            alpha=0.85, width=0.5)
axes[1].set_title("Headcount vs Attrition"); axes[1].set_ylabel("Employees")
axes[1].legend()
plt.tight_layout()
plt.savefig(f"{ASSETS}/02_attrition_by_department.png", bbox_inches="tight")
plt.close()
print("  [Saved] 02_attrition_by_department.png")

# ═══════════════════════════════════════════════════════════════════════════
# 4. ATTRITION BY JOB ROLE
# ═══════════════════════════════════════════════════════════════════════════
role = (df.groupby("JobRole")["Attrition_Flag"]
        .mean().sort_values(ascending=False) * 100).reset_index()
role.columns = ["JobRole", "AttritionRate"]

fig, ax = plt.subplots(figsize=(12, 6))
colors = [RED if v > attr_rate else "#2E86AB" for v in role["AttritionRate"]]
bars = ax.barh(role["JobRole"][::-1], role["AttritionRate"][::-1],
               color=colors[::-1], edgecolor="white")
ax.axvline(attr_rate, color="gray", linestyle="--", linewidth=1.5,
           label=f"Overall avg ({attr_rate:.1f}%)")
ax.set_title("Attrition Rate by Job Role", fontsize=13, fontweight="bold", color=BLUE)
ax.set_xlabel("Attrition Rate (%)")
ax.legend()
for bar, val in zip(bars, role["AttritionRate"][::-1]):
    ax.text(val + 0.3, bar.get_y() + bar.get_height()/2,
            f"{val:.1f}%", va="center", fontsize=9)
plt.tight_layout()
plt.savefig(f"{ASSETS}/03_attrition_by_jobrole.png", bbox_inches="tight")
plt.close()
print("  [Saved] 03_attrition_by_jobrole.png")

# ═══════════════════════════════════════════════════════════════════════════
# 5. AGE DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Age Analysis", fontsize=14, fontweight="bold", color=BLUE)

for label, color in [("No", "#2E86AB"), ("Yes", RED)]:
    axes[0].hist(df[df.Attrition == label]["Age"], bins=20,
                 alpha=0.65, color=color, edgecolor="white",
                 label="Stayed" if label == "No" else "Left")
axes[0].set_title("Age Distribution: Left vs Stayed")
axes[0].set_xlabel("Age"); axes[0].set_ylabel("Count"); axes[0].legend()

# Age group attrition rate
df["AgeGroup"] = pd.cut(df["Age"], bins=[18, 25, 35, 45, 60],
                         labels=["18-25", "26-35", "36-45", "46-60"])
age_grp = (df.groupby("AgeGroup")["Attrition_Flag"]
           .mean().reset_index())
age_grp["rate"] = age_grp["Attrition_Flag"] * 100
axes[1].bar(age_grp["AgeGroup"].astype(str), age_grp["rate"],
            color=[RED, ORANGE, "#2E86AB", GREEN], width=0.5, edgecolor="white")
axes[1].set_title("Attrition Rate by Age Group")
axes[1].set_ylabel("Attrition Rate (%)")
axes[1].axhline(attr_rate, color="gray", linestyle="--", linewidth=1.2)
for i, v in enumerate(age_grp["rate"]):
    axes[1].text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=10)
plt.tight_layout()
plt.savefig(f"{ASSETS}/04_age_analysis.png", bbox_inches="tight")
plt.close()
print("  [Saved] 04_age_analysis.png")

# ═══════════════════════════════════════════════════════════════════════════
# 6. INCOME ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Monthly Income Analysis", fontsize=14, fontweight="bold", color=BLUE)

sns.boxplot(data=df, x="Attrition", y="MonthlyIncome",
            palette=PALETTE, ax=axes[0], width=0.4)
axes[0].set_title("Income Distribution by Attrition")
axes[0].set_xlabel("Attrition (Yes=Left)"); axes[0].set_ylabel("Monthly Income (₹)")
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))

income_dept = df.groupby(["Department", "Attrition"])["MonthlyIncome"].mean().unstack()
income_dept.plot(kind="bar", ax=axes[1], color=[RED, "#2E86AB"],
                 edgecolor="white", width=0.6)
axes[1].set_title("Avg Income by Dept & Attrition")
axes[1].set_ylabel("Avg Monthly Income (₹)")
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=15, ha="right")
axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
axes[1].legend(["Left", "Stayed"])
plt.tight_layout()
plt.savefig(f"{ASSETS}/05_income_analysis.png", bbox_inches="tight")
plt.close()
print("  [Saved] 05_income_analysis.png")

# ═══════════════════════════════════════════════════════════════════════════
# 7. SATISFACTION SCORES
# ═══════════════════════════════════════════════════════════════════════════
sat_cols = ["JobSatisfaction", "EnvironmentSatisfaction",
            "WorkLifeBalance", "JobInvolvement"]
sat_labels = ["Job Satisfaction", "Env. Satisfaction",
              "Work-Life Balance", "Job Involvement"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Satisfaction Scores vs Attrition", fontsize=14, fontweight="bold", color=BLUE)
axes = axes.flatten()

for ax, col, lbl in zip(axes, sat_cols, sat_labels):
    grp = (df.groupby(col)["Attrition_Flag"].mean() * 100).reset_index()
    grp.columns = [col, "rate"]
    bar_colors = [RED if v > attr_rate else "#2E86AB" for v in grp["rate"]]
    ax.bar(grp[col].astype(str), grp["rate"], color=bar_colors, width=0.5, edgecolor="white")
    ax.set_title(f"{lbl} vs Attrition Rate", fontsize=11)
    ax.set_xlabel("Score (1=Low, 4=High)"); ax.set_ylabel("Attrition Rate (%)")
    ax.axhline(attr_rate, color="gray", linestyle="--", linewidth=1.2)
    for i, v in enumerate(grp["rate"]):
        ax.text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=10)

plt.tight_layout()
plt.savefig(f"{ASSETS}/06_satisfaction_scores.png", bbox_inches="tight")
plt.close()
print("  [Saved] 06_satisfaction_scores.png")

# ═══════════════════════════════════════════════════════════════════════════
# 8. OVERTIME & BUSINESS TRAVEL
# ═══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Overtime & Business Travel Impact", fontsize=14, fontweight="bold", color=BLUE)

# Overtime
ot = df.groupby("OverTime")["Attrition_Flag"].mean().reset_index()
ot["rate"] = ot["Attrition_Flag"] * 100
axes[0].bar(ot["OverTime"], ot["rate"], color=[RED, "#2E86AB"], width=0.4, edgecolor="white")
axes[0].set_title("Attrition Rate by Overtime")
axes[0].set_ylabel("Attrition Rate (%)")
axes[0].axhline(attr_rate, color="gray", linestyle="--", linewidth=1.2)
for i, v in enumerate(ot["rate"]):
    axes[0].text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=12, fontweight="bold")

# Business Travel
bt = (df.groupby("BusinessTravel")["Attrition_Flag"].mean() * 100).sort_values(ascending=False).reset_index()
bt.columns = ["BusinessTravel", "rate"]
axes[1].bar(bt["BusinessTravel"], bt["rate"],
            color=[RED, ORANGE, "#2E86AB"], width=0.4, edgecolor="white")
axes[1].set_title("Attrition Rate by Business Travel")
axes[1].set_ylabel("Attrition Rate (%)")
axes[1].axhline(attr_rate, color="gray", linestyle="--", linewidth=1.2)
axes[1].set_xticklabels(bt["BusinessTravel"], rotation=10)
for i, v in enumerate(bt["rate"]):
    axes[1].text(i, v + 0.5, f"{v:.1f}%", ha="center", fontsize=11, fontweight="bold")

plt.tight_layout()
plt.savefig(f"{ASSETS}/07_overtime_travel.png", bbox_inches="tight")
plt.close()
print("  [Saved] 07_overtime_travel.png")

# ═══════════════════════════════════════════════════════════════════════════
# 9. YEARS AT COMPANY & TENURE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Tenure & Years Analysis", fontsize=14, fontweight="bold", color=BLUE)

for label, color in [("No", "#2E86AB"), ("Yes", RED)]:
    axes[0].hist(df[df.Attrition == label]["YearsAtCompany"], bins=20,
                 alpha=0.65, color=color, edgecolor="white",
                 label="Stayed" if label=="No" else "Left")
axes[0].set_title("Years at Company: Left vs Stayed")
axes[0].set_xlabel("Years at Company"); axes[0].set_ylabel("Count")
axes[0].legend()

sns.boxplot(data=df, x="Department", y="YearsAtCompany",
            hue="Attrition", palette=PALETTE, ax=axes[1], width=0.5)
axes[1].set_title("Years at Company by Department")
axes[1].set_xlabel("Department"); axes[1].set_ylabel("Years at Company")
axes[1].legend(title="Attrition", labels=["Stayed","Left"])
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=10)
plt.tight_layout()
plt.savefig(f"{ASSETS}/08_tenure_analysis.png", bbox_inches="tight")
plt.close()
print("  [Saved] 08_tenure_analysis.png")

# ═══════════════════════════════════════════════════════════════════════════
# 10. CORRELATION HEATMAP
# ═══════════════════════════════════════════════════════════════════════════
num_cols = ["Age", "MonthlyIncome", "TotalWorkingYears", "YearsAtCompany",
            "JobSatisfaction", "WorkLifeBalance", "EnvironmentSatisfaction",
            "DistanceFromHome", "NumCompaniesWorked", "Attrition_Flag"]
corr = df[num_cols].corr()

fig, ax = plt.subplots(figsize=(11, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0,
            mask=mask, ax=ax, linewidths=0.5, square=True,
            cbar_kws={"shrink": 0.8})
ax.set_title("Correlation Heatmap — Numerical Features",
             fontsize=13, fontweight="bold", color=BLUE)
plt.tight_layout()
plt.savefig(f"{ASSETS}/09_correlation_heatmap.png", bbox_inches="tight")
plt.close()
print("  [Saved] 09_correlation_heatmap.png")

# ═══════════════════════════════════════════════════════════════════════════
# 11. MARITAL STATUS & GENDER
# ═══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Demographics Impact on Attrition", fontsize=14, fontweight="bold", color=BLUE)

for ax, col, title in zip(axes, ["MaritalStatus","Gender"],
                          ["Attrition by Marital Status","Attrition by Gender"]):
    grp = (df.groupby(col)["Attrition_Flag"].mean()*100).sort_values(ascending=False).reset_index()
    grp.columns = [col, "rate"]
    bar_colors = [RED if v > attr_rate else "#2E86AB" for v in grp["rate"]]
    ax.bar(grp[col], grp["rate"], color=bar_colors, width=0.4, edgecolor="white")
    ax.set_title(title, fontsize=11); ax.set_ylabel("Attrition Rate (%)")
    ax.axhline(attr_rate, color="gray", linestyle="--", linewidth=1.2)
    for i, v in enumerate(grp["rate"]):
        ax.text(i, v+0.5, f"{v:.1f}%", ha="center", fontsize=11, fontweight="bold")

plt.tight_layout()
plt.savefig(f"{ASSETS}/10_demographics.png", bbox_inches="tight")
plt.close()
print("  [Saved] 10_demographics.png")

# ═══════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  ATTRITION ANALYSIS SUMMARY")
print("=" * 60)
print(f"  Overall Attrition Rate  : {attr_rate:.1f}%")
print(f"  Avg Age (Left)          : {df[df.Attrition=='Yes']['Age'].mean():.1f}")
print(f"  Avg Age (Stayed)        : {df[df.Attrition=='No']['Age'].mean():.1f}")
print(f"  Avg Income (Left)       : ₹{df[df.Attrition=='Yes']['MonthlyIncome'].mean():,.0f}")
print(f"  Avg Income (Stayed)     : ₹{df[df.Attrition=='No']['MonthlyIncome'].mean():,.0f}")
ot_yes = df[df.OverTime=='Yes']['Attrition_Flag'].mean()*100
ot_no  = df[df.OverTime=='No']['Attrition_Flag'].mean()*100
print(f"  Attrition (Overtime=Yes): {ot_yes:.1f}%")
print(f"  Attrition (Overtime=No) : {ot_no:.1f}%")
print("\n  [✓] All 10 charts saved to /assets/")
print("=" * 60)
