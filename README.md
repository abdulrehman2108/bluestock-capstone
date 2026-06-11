# Bluestock Mutual Fund Analytics Platform

## End-to-End Data Engineering, Financial Analytics & Business Intelligence Solution

## Project Overview

The Bluestock Mutual Fund Analytics Platform is an end-to-end Data Analytics and Business Intelligence project designed to analyze mutual fund performance, investor behavior, portfolio allocation, and benchmark market trends.

The project demonstrates a complete analytics lifecycle, including data acquisition, ETL pipeline development, data cleaning and transformation, database management, financial performance analytics, and interactive dashboard development.

Using Python, Pandas, MySQL, SQL, and Power BI, raw financial datasets are transformed into actionable business insights that support investment analysis and decision-making.

---

## Business Objective

The primary objectives of this project are:

* Analyze mutual fund performance across multiple schemes.
* Evaluate risk-adjusted returns using financial metrics.
* Understand investor demographics and investment behavior.
* Compare mutual fund performance against benchmark indices.
* Build interactive dashboards for business intelligence reporting.
* Deliver fund-level insights through drill-through analysis.

---

## Project Architecture

```text
Raw Data Sources
        ↓
Data Acquisition
        ↓
ETL Pipeline
        ↓
Data Cleaning & Transformation
        ↓
MySQL Database
        ↓
Financial Analytics
        ↓
Power BI Dashboard
        ↓
Business Insights
```

---

## Technology Stack

### Data Engineering

* Python
* Pandas
* NumPy
* MySQL
* SQL

### Analytics

* Financial Performance Analytics
* Risk Analysis
* Benchmark Comparison

### Business Intelligence

* Power BI
* DAX
* Data Modeling

### Version Control

* Git
* GitHub

---

## Datasets Used

### Fund Master

Contains scheme metadata including:

* AMFI Code
* Scheme Name
* Fund House
* Category
* Plan Type

### NAV History

Contains historical Net Asset Value (NAV) records for mutual fund schemes.

### Scheme Performance

Contains:

* Returns
* Expense Ratios
* Assets Under Management (AUM)

### Investor Transactions

Contains:

* SIP Investments
* Lumpsum Investments
* Redemptions
* State Information
* Age Groups
* City Tier Information

### Portfolio Holdings

Contains:

* Portfolio Allocation
* Sector Exposure
* Holdings Information

### Benchmark Indices

Contains benchmark market information including:

* NIFTY 50
* Historical Market Trends

---

## ETL Pipeline

### Extract

Collected raw mutual fund datasets and benchmark data.

### Transform

Data cleaning activities included:

* Missing Value Handling
* Duplicate Removal
* Date Standardization
* Data Type Conversion
* Column Normalization
* Validation Checks

### Load

Cleaned datasets were loaded into MySQL for analytical processing.

---

## Database Design

### Database

```sql
bluestock_mf
```

### Core Tables

* fund_master
* nav_history
* scheme_performance
* investor_transactions
* portfolio_holdings
* benchmark_indices

### Database Scripts

* schema.sql
* queries.sql

### Primary Relationship Key

```text
amfi_code
```

The AMFI Code was used to establish relationships across datasets and support integrated analysis.

---

## Financial Performance Analytics

The project implements industry-standard mutual fund performance metrics.

### Daily Return

```text
Daily Return = (NAVt / NAVt-1) - 1
```

### CAGR

```text
CAGR = (Ending NAV / Beginning NAV)^(1/n) - 1
```

### Volatility

```text
Volatility = Standard Deviation of Daily Returns
```

### Sharpe Ratio

```text
Sharpe Ratio = (Rp - Rf) / σ × √252
```

Risk-Free Rate Assumption:

```text
6.5%
```

### Sortino Ratio

Measures return relative to downside risk.

### Alpha

Measures fund outperformance relative to benchmark expectations.

### Beta

Measures fund sensitivity to market movements.

### Maximum Drawdown

Measures the largest decline from peak to trough.

---

## Fund Scorecard Framework

A composite scoring model was developed using:

* CAGR
* Sharpe Ratio
* Alpha
* Expense Ratio
* Maximum Drawdown

The scorecard enables ranking and comparison of mutual fund schemes using a single performance indicator.

---

## Exploratory Data Analysis

The project includes extensive exploratory analysis covering:

### Fund Analysis

* Category Distribution
* Fund House Analysis
* Scheme Composition

### Investor Analysis

* State-wise Investment Distribution
* Age Group Analysis
* T30 vs B30 Analysis

### Transaction Analysis

* SIP Trends
* Redemption Analysis
* Investment Activity Trends

### Portfolio Analysis

* Sector Allocation
* Portfolio Concentration
* Diversification Analysis

### Market Analysis

* NIFTY 50 Trends
* Benchmark Performance Analysis

---

## Power BI Dashboard

### Page 1 — Industry Overview

Key Metrics:

* Total AUM
* Total Schemes
* SIP Contributions
* Industry KPIs

Visuals:

* Industry Trend Analysis
* AUM Distribution
* KPI Cards

---

### Page 2 — Fund Performance

Visuals:

* Risk vs Return Scatter Plot
* Fund Scorecard Rankings
* Top Performing Funds
* Sharpe Ratio Analysis

---

### Page 3 — Investor Analytics

Visuals:

* State-wise Investment Analysis
* Age Group Distribution
* T30 vs B30 Comparison
* Transaction Trends

---

### Page 4 — SIP & Market Trends

Visuals:

* SIP Growth Trends
* Benchmark Comparison
* Category Allocation Analysis
* Market Participation Insights

---

### Page 5 — Fund Detail Drill-Through

Features:

* Dynamic Fund Selection
* CAGR
* Sharpe Ratio
* Alpha
* Maximum Drawdown
* Fund Score
* NAV Performance Trend
* Benchmark Comparison
* Risk Metrics

---

## Key Insights

* Risk-adjusted returns vary significantly across mutual fund schemes.
* SIP contributions remain relatively stable despite market fluctuations.
* Investment participation is concentrated in specific geographic regions.
* Benchmark comparison provides deeper insight than absolute returns alone.
* Portfolio allocation significantly influences fund risk characteristics.

---

## Repository Structure

```text
project/

├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebooks/
│   ├── live_fetch_nav.ipynb
│   ├── ETL_Pipeline.ipynb
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── database/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboards/
│   └── Bluestock_m.pbix
│
├── reports/
│   ├── Project_Report.pdf
│   └── Presentation.pptx
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

## How to Run the Project

### Clone Repository

```bash
git clone <repository_url>
cd bluestock-mutual-fund-analytics
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python etl_pipeline.py
```

### Create Database

```bash
mysql -u username -p
```

```sql
CREATE DATABASE bluestock_mf;
USE bluestock_mf;
SOURCE database/schema.sql;
```

### Execute Analytical Queries

```sql
SOURCE database/queries.sql;
```

### Open Dashboard

Open:

```text
Bluestock_mf.pbix
```

using Power BI Desktop.

---

## Future Enhancements

* Real-Time API Integration
* Automated Data Refresh
* Predictive Fund Performance Models
* Portfolio Optimization Engine
* Advanced Investor Segmentation
* Machine Learning-Based Fund Recommendations

---

## Author

**Abdul Rehman Ansari**

Bachelor of Science in Information Technology (B.Sc. IT)

Data Analytics | Business Intelligence | Python | SQL | MySQL | Power BI

---

## License

This project is intended for educational, portfolio, and demonstration purposes under internship of Bluestock.
