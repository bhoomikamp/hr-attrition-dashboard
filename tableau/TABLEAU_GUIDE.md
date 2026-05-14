# Tableau Dashboard — Setup Guide
## HR Analytics: Employee Attrition

---

## Step 1: Connect to the Dataset

1. Open **Tableau Desktop** (or Tableau Public — free version)
2. Click **Connect → Text File**
3. Select `data/hr_attrition.csv`
4. Tableau auto-detects all column types — verify:
   - `EmployeeNumber` → Number (Whole)
   - `Age`, `MonthlyIncome`, `YearsAtCompany` → Number (Whole)
   - `JobSatisfaction`, `WorkLifeBalance`, etc. → Number (Whole)
   - `Attrition`, `Department`, `JobRole` → String
5. Click **Sheet 1** to start building

---

## Step 2: Create Calculated Fields

Go to **Analysis → Create Calculated Field** for each:

```tableau
-- Attrition Flag (1/0)
Name: [Attrition Flag]
Formula: IF [Attrition] = "Yes" THEN 1 ELSE 0 END

-- Attrition Rate %
Name: [Attrition Rate %]
Formula: SUM([Attrition Flag]) / COUNT([Employee Number]) * 100

-- Age Group
Name: [Age Group]
Formula:
IF [Age] <= 25 THEN "18-25"
ELSEIF [Age] <= 35 THEN "26-35"
ELSEIF [Age] <= 45 THEN "36-45"
ELSE "46-60"
END

-- Salary Band
Name: [Salary Band]
Formula:
IF [Monthly Income] < 5000 THEN "Low (<5K)"
ELSEIF [Monthly Income] < 10000 THEN "Mid (5K-10K)"
ELSEIF [Monthly Income] < 20000 THEN "High (10K-20K)"
ELSE "Very High (>20K)"
END

-- Tenure Bucket
Name: [Tenure Bucket]
Formula:
IF [Years At Company] < 2 THEN "0-1 years"
ELSEIF [Years At Company] < 5 THEN "2-4 years"
ELSEIF [Years At Company] < 10 THEN "5-9 years"
ELSE "10+ years"
END

-- Risk Score (for risk segment sheet)
Name: [Risk Score]
Formula:
(IF [Over Time] = "Yes" THEN 2 ELSE 0 END) +
(IF [Job Satisfaction] <= 2 THEN 2 ELSE 0 END) +
(IF [Work Life Balance] <= 2 THEN 1 ELSE 0 END) +
(IF [Business Travel] = "Travel_Frequently" THEN 1 ELSE 0 END) +
(IF [Years At Company] < 3 THEN 1 ELSE 0 END)
```

---

## Step 3: Build Dashboard Pages

### 📊 Sheet 1 — KPI Summary (Text Table)
| Setting | Value |
|---------|-------|
| Row | (empty — use text marks) |
| Use Show Me → Text Table | |
| Add KPI Cards for | Total Employees, Attrition Rate %, Avg Income (Left), Avg Tenure |

**How to make KPI Cards:**
1. Drag `Number of Records` to Text
2. Right-click → Add Table Calculation → custom
3. Duplicate sheet for each KPI and format as big bold number

---

### 📊 Sheet 2 — Attrition by Department (Bar Chart)
| Field | Shelf |
|-------|-------|
| `Department` | Columns |
| `Attrition Rate %` (calculated) | Rows |
| `Attrition` | Color |
| `Attrition Rate %` | Label |

**Steps:**
1. Drag `Department` to Columns
2. Drag `Attrition Flag` to Rows → Right-click → Measure → Average → multiply by 100 OR use calculated field
3. Drag `Attrition` to Color shelf
4. Sort bars descending

---

### 📊 Sheet 3 — Attrition by Job Role (Horizontal Bar)
| Field | Shelf |
|-------|-------|
| `Attrition Rate %` | Columns |
| `Job Role` | Rows |
| `Attrition Rate %` | Color (gradient) |
| `Attrition Rate %` | Label |

**Steps:**
1. Drag `Job Role` to Rows
2. Drag `Attrition Flag` (AVG → ×100) to Columns
3. Sort descending by attrition rate
4. Format → Color → Red-Blue Diverging

---

### 📊 Sheet 4 — Age Distribution Histogram
| Field | Shelf |
|-------|-------|
| `Age` | Columns (bin it: right-click → Create → Bins → size 5) |
| `Number of Records` | Rows |
| `Attrition` | Color |

**Steps:**
1. Right-click `Age` → Create → Bins → Bin size = 5
2. Drag `Age (bin)` to Columns
3. Drag `Number of Records` to Rows
4. Drag `Attrition` to Color

---

### 📊 Sheet 5 — Income Box Plot
| Field | Shelf |
|-------|-------|
| `Attrition` | Columns |
| `Monthly Income` | Rows |
| Show Me → Box-and-Whisker Plot | |
| `Department` | Pages (to filter by dept) |

---

### 📊 Sheet 6 — Satisfaction Heatmap
| Field | Shelf |
|-------|-------|
| `Job Satisfaction` | Columns |
| `Job Role` | Rows |
| `Attrition Rate %` | Color (Red-White-Green) |
| `Attrition Rate %` | Label |

---

### 📊 Sheet 7 — Overtime Impact (Side-by-Side Bar)
| Field | Shelf |
|-------|-------|
| `Over Time` | Columns |
| `Attrition Rate %` | Rows |
| `Department` | Color |

---

### 📊 Sheet 8 — Tenure Analysis (Line Chart)
| Field | Shelf |
|-------|-------|
| `Tenure Bucket` | Columns |
| `Attrition Rate %` | Rows |
| `Department` | Color |
| `Attrition Rate %` | Label |

---

## Step 4: Build the Main Dashboard

1. Click **New Dashboard** (bottom tab)
2. Set size: **1200 × 800px** (fixed)
3. Drag sheets onto the canvas in this layout:

```
┌─────────────────────────────────────────────────────┐
│  KPI CARDS: Total Emp | Attrition% | AvgIncome      │
├──────────────────┬──────────────────────────────────┤
│  By Department   │    By Job Role (horizontal)      │
├──────────────────┼──────────────────────────────────┤
│  Age Histogram   │    Satisfaction Heatmap          │
├──────────────────┴──────────────────────────────────┤
│  Overtime Bar  |  Tenure Line  |  Income Boxplot    │
└─────────────────────────────────────────────────────┘
```

---

## Step 5: Add Filters (Interactive Slicers)

Right-click each of these fields → **Show Filter**:
- `Department`
- `Gender`
- `Age Group` (calculated)
- `OverTime`
- `MaritalStatus`
- `BusinessTravel`

Set filter style to **Multiple Values (dropdown)** for cleaner look.

---

## Step 6: Formatting Tips

- **Color Palette:** Use Red (`#C73E1D`) for "Attrition=Yes", Blue (`#2E86AB`) for "No"
- **Fonts:** Tableau Book, size 10-12 for labels, size 18-20 for KPI numbers
- **Grid lines:** Format → Lines → set to light gray
- **Title:** Each sheet title should describe the insight, e.g. *"Sales Dept has 34.7% attrition — highest across all departments"*
- **Tooltips:** Edit tooltip on each sheet to show Department, Role, Income, and Attrition Rate

---

## Step 7: Publish to Tableau Public (Free)

1. File → Save to Tableau Public
2. Sign in / create a free account at **public.tableau.com**
3. Your dashboard is now live with a shareable URL
4. Add the link to your GitHub README and resume!

---

## Dashboard Preview

All Python-generated charts in `/assets/` mirror the exact visuals
you will build in Tableau. Use them as a reference guide.
