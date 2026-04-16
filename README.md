# Career Finance Tradeoff Analysis

A data-driven project analyzing career, salary, and geographic tradeoffs across the U.S. and China, focusing on higher education vs data/tech roles.

---

## 🎯 Project Goal

This project explores:

> How do career path and location impact financial outcomes?

Specifically:
- Compare higher education vs data/tech roles
- Compare U.S. (Texas) vs China (Shanghai, Suzhou)
- Normalize salary data across currencies and pay structures
- Build a foundation for financial modeling (savings, projections)

---

## 🧱 Current Progress (Day 1)

### ✅ Salary Data Pipeline — Completed

Built a full pipeline from raw data to a cleaned, standardized dataset.

### 1. Data Collection

Collected salary data from:
- U.S. Bureau of Labor Statistics (BLS)
- BOSS直聘 job listings (China)

Raw data stored in: `data/raw/salary_raw.csv`

Includes:
- salary ranges (low / high)
- currency (USD / CNY)
- period (monthly / yearly)
- pay structure (`pay_months`)
- source tracking

---

### 2. Data Cleaning & Transformation

Implemented in: `src/clean_salary_data.py`

Pipeline performs:
- Convert monthly → annual salary
- Handle pay structures (e.g., 12 vs 14 months)
- Compute median salary from ranges
- Normalize currency (USD ↔ CNY)

---

### 3. Output Dataset

Generated: `data/processed/salary_cleaned.csv`

Key fields:
- `median_annual_local`
- `median_annual_usd`
- `median_annual_cny`

---

## 📊 Sample Output

| Location  | Role                | Median Annual (USD) |
|-----------|---------------------|---------------------|
| Texas     | Software Developer  | ~131k               |
| Texas     | HigherEd Admin      | ~106k               |
| Shanghai  | Data Engineer       | ~61k                |
| Shanghai  | HigherEd Admin      | ~30k                |
| Suzhou    | Data Engineer       | ~50k                |
| Suzhou    | HigherEd Admin      | ~18k                |

---

## 🧠 Key Early Insights

- In the U.S., higher education and data roles have similar salary ranges
- In China, data roles significantly out-earn higher education roles
- Absolute salaries remain higher in the U.S. across all roles

---

## 🗂 Project Structure
```text
career-finance-tradeoff-analysis/
├── data/
│   ├── raw/
│   │   ├── salary_raw.csv
│   │   └── cost_of_living_raw.csv
│   └── processed/
│       └── salary_cleaned.csv
├── data/source_docs/
│   └── (BOSS job listing PDFs)
├── src/
│   └── clean_salary_data.py
├── outputs/
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack
 - Python 3.13
- pandas
- matplotlib (planned)

---

## 🛠 How to Run
1. Create virtual environment:
    - `python3 -m venv .venv`
    - `source .venv/bin/activate`
2. Install dependencies:
`pip install -r requirements.txt`
3. Run the pipeline:
`python main.py`

---

## 📌 Data Notes
- Salary data is aggregated from public sources and job listings
- China salary data is averaged from multiple listings
- Exchange rate is standardized for comparison
- This project focuses on structured modeling rather than exact prediction
---
## 🚀 Next Steps
### Phase 2 — Cost of Living
- Collect rent, food, and transportation cost data
- Build cost-of-living dataset
### Phase 3 — Financial Modeling
- Calculate monthly savings
- Compare purchasing power across locations
### Phase 4 — Visualization
- Salary comparison charts
- Savings comparison charts
- 3-year and 10-year projections


