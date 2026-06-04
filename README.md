# Bluestock Mutual Fund Analytics Warehouse

## Project Overview

Bluestock Mutual Fund Analytics Warehouse is a financial data engineering and analytics project designed to process, clean, transform, and analyze mutual fund datasets using a star schema warehouse architecture.

The project focuses on:

* Mutual fund performance analytics
* NAV trend analysis
* Investor transaction analysis
* AUM-based fund insights
* SQL-based business intelligence reporting

The complete pipeline includes:

* Data ingestion
* Data cleaning and transformation
* Warehouse schema modeling
* ETL loading
* Analytical SQL querying

---

# Tech Stack

| Technology       | Purpose                           |
| ---------------- | --------------------------------- |
| Python           | Data processing and ETL           |
| Pandas           | Data cleaning and transformation  |
| MySQL            | Data warehouse storage            |
| SQLAlchemy       | Python ↔ MySQL integration        |
| Jupyter Notebook | Exploratory analysis and cleaning |
| SQL              | Analytical querying               |

---

# Project Architecture

```text
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
Analytical SQL Queries
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
* Time-series NAV analytics
* Investor transaction analytics
* Mutual fund performance benchmarking
* Risk-adjusted fund analysis
* Star schema warehouse design
* SQL-based KPI generation

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

---

# Project Structure

```text
Bluestock_capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   └── live_nav_fetch.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
│   └── data_dictionary.md
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
* Metric validation
* Missing value handling

## 3. Warehouse Transformation

* Fact table creation
* Dimension table generation
* Schema alignment

## 4. Data Loading

* Processed datasets loaded into MySQL warehouse

---

# Data Sources

This project uses:

* Mutual fund metadata
* Historical NAV data
* Investor transaction datasets
* Fund performance metrics

Note:
Actual source datasets and credentials are intentionally excluded from the repository for confidentiality and security purposes.

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
cd Bluestock_capstone
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure MySQL

Create database:

```sql
CREATE DATABASE bluestock_mf;
```

Run:

* `sql/schema.sql`

---

## Execute ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

---

# Security & Confidentiality

The repository intentionally excludes:

* Database credentials
* Local system paths
* Raw confidential datasets
* Database binary files
* Environment configurations

Database files such as:

* `.db`
* `.sqlite`
* `.sqlitedb`

are excluded using `.gitignore`.

---

# Future Enhancements

* Power BI dashboard integration
* Automated scheduled ETL
* Incremental data loading
* Streamlit analytics app
* Advanced portfolio analytics
* Cloud warehouse deployment

---

# Author

Abdul Rehman Ansari

BSc IT — Data Analytics & Engineering Project

