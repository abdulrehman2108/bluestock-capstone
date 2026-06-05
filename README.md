# Bluestock Mutual Fund Analytics Warehouse

## Project Overview

Bluestock Mutual Fund Analytics Warehouse is an end-to-end financial data engineering and analytics project designed to process, clean, transform, and analyze mutual fund datasets using a star schema warehouse architecture.

The project focuses on:

* NAV trend analysis
* Mutual fund performance analytics
* Investor transaction analysis
* SIP inflow analysis
* Risk-adjusted fund comparison
* Sector allocation analysis
* SQL-based business intelligence reporting

The project workflow includes:

* Data ingestion
* Data cleaning and transformation
* ETL pipeline creation
* Star schema warehouse modeling
* MySQL data loading
* Exploratory Data Analysis (EDA)
* Analytical SQL querying

---

# Tech Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Data processing & ETL          |
| Pandas           | Data cleaning & transformation |
| NumPy            | Numerical computations         |
| Matplotlib       | Data visualization             |
| Seaborn          | Statistical visualization      |
| Plotly           | Interactive visualizations     |
| MySQL            | Data warehouse storage         |
| SQLAlchemy       | Python ↔ MySQL integration     |
| Jupyter Notebook | EDA & analysis                 |
| SQL              | Analytical querying            |

---

# Project Architecture

```text id="tbdqqq"
Raw CSV Data
      ↓
Data Cleaning & Transformation (Pandas)
      ↓
Warehouse-Ready Fact & Dimension Tables
      ↓
ETL Pipeline
      ↓
MySQL Star Schema Warehouse
      ↓
EDA & Analytical SQL Queries
      ↓
Dashboard / Reporting Layer
```

---

# Star Schema Design

## Dimension Tables

* `dim_fund`
* `dim_date`

## Fact Tables

* `fact_nav`
* `fact_transactions`
* `fact_performance`
* `fact_aum`

---

# Key Features

* Data cleaning and normalization using Pandas
* Historical NAV trend analysis
* SIP inflow trend analysis
* Investor demographics analysis
* Geographic investment distribution analysis
* Correlation analysis between mutual funds
* Sector allocation analytics
* SQL-based KPI generation
* Star schema warehouse implementation

---

# Exploratory Data Analysis (EDA)

The project includes:

* 15+ visualizations
* Plotly interactive charts
* Seaborn statistical plots
* Time-series NAV analysis
* Correlation heatmaps
* Investor demographic analysis
* SIP inflow analysis
* Sector allocation donut charts

---

# Analytical SQL Use Cases

The warehouse supports:

* Top funds by AUM
* Monthly NAV trend analysis
* SIP growth analysis
* State-wise investment analysis
* Expense ratio analysis
* Risk-adjusted performance ranking
* Fund category distribution
* Sharpe ratio analysis

---

# Project Structure

```text id="nmmgmd"
Bluestock_capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── EDA_Analysis.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── create_sqlite_db.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
│   └── data_dictionary.md
│
├── dashboard/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ETL Workflow

## 1. Data Ingestion

* Raw mutual fund datasets loaded using Pandas
* Live NAV data fetched using API integration

## 2. Data Cleaning

* Duplicate removal
* Date parsing
* Datatype standardization
* Missing value handling
* Financial metric validation

## 3. Warehouse Transformation

* Fact table creation
* Dimension table generation
* Schema alignment
* Star schema modeling

## 4. Data Loading

* Processed datasets loaded into MySQL warehouse

## 5. EDA & Analytics

* Trend analysis
* Correlation analysis
* Investor insights
* Geographic analysis
* Risk-performance analytics

---

# Datasets Used

| Dataset                   | Description                  |
| ------------------------- | ---------------------------- |
| fund_master.csv           | Mutual fund scheme metadata  |
| nav_history.csv           | Historical NAV data          |
| investor_transactions.csv | Investor transaction records |
| scheme_performance.csv    | Fund performance metrics     |
| portfolio_holdings.csv    | Portfolio sector allocation  |

---

# Setup Instructions

## Clone Repository

```bash id="mvurxm"
git clone <repository-url>
cd Bluestock_capstone
```

---

## Install Dependencies

```bash id="wdwkxm"
pip install -r requirements.txt
```

---

## Configure MySQL

Create database:

```sql id="rnbhfj"
CREATE DATABASE bluestock_mf;
```

Run:

* `sql/schema.sql`

---

## Execute ETL Pipeline

```bash id="ynrxxz"
python scripts/etl_pipeline.py
```

---

## Run EDA Notebook

Open:

```text id="chpqcg"
notebooks/EDA_Analysis.ipynb
```

Execute all cells sequentially.

---

# Security & Confidentiality

This repository intentionally excludes:

* Database credentials
* Local system paths
* Raw confidential datasets
* Database binary files
* Environment configuration files

Database files such as:

* `.db`
* `.sqlite`
* `.sqlitedb`

are excluded using `.gitignore`.

---

# Future Enhancements

* Power BI dashboard integration
* Streamlit analytics dashboard
* Automated scheduled ETL
* Incremental data loading
* Cloud warehouse deployment
* Portfolio optimization analytics

---

# Author

Abdul Rehman Ansari

BSc IT — Data Analytics & Engineering Project
