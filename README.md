# Bluestock Mutual Fund Analytics Warehouse

## Project Overview

Bluestock Mutual Fund Analytics Warehouse is an end-to-end financial analytics and data engineering project focused on mutual fund performance analysis, investor behavior analytics, and quantitative portfolio evaluation.

The project integrates:

* Data ingestion pipelines
* ETL workflows
* MySQL star-schema warehouse modeling
* Exploratory Data Analysis (EDA)
* Quantitative financial analytics
* Portfolio performance benchmarking

The system processes multiple mutual fund datasets including:

* NAV history
* Scheme performance
* Investor transactions
* Fund metadata
* Portfolio holdings

and transforms them into business-ready analytical insights.

---

# Objectives

The project aims to:

* Build a scalable mutual fund analytics pipeline
* Clean and standardize raw financial datasets
* Design a star-schema warehouse model
* Perform quantitative portfolio analytics
* Generate risk-adjusted fund rankings
* Analyze investor and SIP behavior
* Benchmark funds against market performance

---

# Tech Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Data engineering & analytics   |
| Pandas           | Data cleaning & transformation |
| NumPy            | Numerical computation          |
| Matplotlib       | Visualization                  |
| Seaborn          | Statistical plotting           |
| Plotly           | Interactive charts             |
| MySQL            | Data warehouse                 |
| SQLAlchemy       | Database integration           |
| SciPy            | Statistical regression         |
| Jupyter Notebook | EDA & analytics                |
| Git & GitHub     | Version control                |

---

# Project Architecture

```text
Raw CSV + API Data
        ↓
Data Cleaning & Validation
        ↓
Processed Analytical Datasets
        ↓
ETL Pipeline
        ↓
MySQL Star Schema Warehouse
        ↓
EDA + Financial Analytics
        ↓
Business Insights & Reporting
```

---

# Datasets Used

| Dataset                   | Description                      |
| ------------------------- | -------------------------------- |
| fund_master.csv           | Fund metadata and classification |
| nav_history.csv           | Daily NAV history                |
| investor_transactions.csv | Investor transaction behavior    |
| scheme_performance.csv    | Fund performance metrics         |
| portfolio_holdings.csv    | Sector allocation & holdings     |

---

# Warehouse Schema

## Dimension Tables

### dim_fund

Contains:

* fund metadata
* categories
* risk classification
* scheme details

### dim_date

Contains:

* calendar attributes
* year/month/quarter mapping

---

## Fact Tables

### fact_nav

Stores:

* daily NAV history
* return analytics base

### fact_transactions

Stores:

* SIPs
* redemptions
* investor activity

### fact_performance

Stores:

* CAGR
* Alpha
* Beta
* Sharpe Ratio
* expense ratio metrics

### fact_aum

Stores:

* Assets Under Management data

---

# ETL Pipeline

The ETL pipeline performs:

* Data ingestion
* Datatype normalization
* Missing-value handling
* Duplicate removal
* Financial metric validation
* Warehouse-ready transformation
* MySQL loading

---

# Exploratory Data Analysis (EDA)

EDA includes:

* NAV trend analysis
* SIP inflow trends
* Investor demographic analysis
* Geographic investment distribution
* Correlation heatmaps
* Sector allocation analysis
* Fund-house comparison
* Portfolio concentration analysis

---

# Quantitative Financial Analytics

The project implements advanced portfolio analytics:

| Metric                   | Purpose                       |
| ------------------------ | ----------------------------- |
| Daily Returns            | Time-series return generation |
| CAGR                     | Long-term growth measurement  |
| Sharpe Ratio             | Risk-adjusted returns         |
| Sortino Ratio            | Downside-risk analysis        |
| Alpha                    | Benchmark outperformance      |
| Beta                     | Market sensitivity            |
| Maximum Drawdown         | Crash-risk evaluation         |
| Tracking Error           | Benchmark deviation           |
| Composite Fund Scorecard | Multi-factor ranking          |

---

# Key Analytics Features

* Risk-adjusted fund ranking
* Benchmark-relative analytics
* Portfolio risk evaluation
* Volatility analysis
* Drawdown analytics
* Mutual fund scorecard system

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
│   ├── data_cleaning.ipynb
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── scripts/
│   ├── live_nav_fetch.py
│   ├__ etl_pipeline.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
│   ├── data_dictionary.md
│   └── charts/
│
├── dashboard/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

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

# MySQL Configuration

Create database:

```sql
CREATE DATABASE bluestock_mf;
```

Run schema:

```sql
SOURCE sql/schema.sql;
```

---

# Execute ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

---

# Run Jupyter Notebooks

```bash
jupyter notebook
```

Open:

* `EDA_Analysis.ipynb`
* `Performance_Analytics.ipynb`

---

# Key Deliverables

| Deliverable                    | Description                    |
| ------------------------------ | ------------------------------ |
| Cleaned CSV datasets           | Processed analytical datasets  |
| MySQL warehouse                | Star-schema implementation     |
| SQL analytical queries         | Business insights              |
| EDA notebook                   | Visualization & exploration    |
| Performance analytics notebook | Quantitative finance analytics |
| fund_scorecard.csv             | Final composite ranking        |
| alpha_beta.csv                 | Regression metrics             |
| README.md                      | Project documentation          |

---

# Security & Confidentiality

The repository excludes:

* database credentials
* local system paths
* temporary notebook checkpoints
* binary database files
* confidential environment variables

The following are ignored using `.gitignore`:

* `.db`
* `__pycache__/`
* `.ipynb_checkpoints/`
* `.env`

---

# Future Enhancements

* Power BI integration
* Streamlit dashboard deployment
* Automated ETL scheduling
* Real-time NAV ingestion
* Cloud warehouse deployment
* Portfolio optimization models
* Advanced factor modeling

---

# Author

Abdul Rehman Ansari

BSc IT — Data Engineering & Financial Analytics Project
