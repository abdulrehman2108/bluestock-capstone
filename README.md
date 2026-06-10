# Bluestock Mutual Fund Analytics Platform

## Overview

The Bluestock Mutual Fund Analytics Platform is an end-to-end data analytics project designed to analyze mutual fund performance, investor behavior, and market trends. The project demonstrates a complete analytics workflow, including data ingestion, cleaning, transformation, database management, financial performance analytics, and interactive dashboard development.

The solution integrates Python, Pandas, SQL, MySQL, and Power BI to transform raw mutual fund datasets into actionable business insights.

---

## Business Objective

The objective of this project is to:

* Analyze mutual fund performance across multiple schemes.
* Evaluate risk-adjusted returns using financial metrics.
* Understand investor demographics and investment behavior.
* Compare SIP investment trends with benchmark market indices.
* Deliver interactive business intelligence dashboards for decision-making.

---

## Project Architecture

Raw CSV Data
↓
Data Cleaning & Validation (Pandas)
↓
ETL Pipeline
↓
SQLite Database
↓
Performance Analytics
↓
Power BI Dashboards
↓
Business Insights

---

## Technology Stack

### Data Engineering

* Python
* Pandas
* NumPy
* SQLite

### Analytics

* Financial Performance Metrics
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

### 1. Fund Master

Contains scheme metadata including:

* AMFI Code
* Scheme Name
* Fund House
* Category
* Plan Type

### 2. NAV History

Daily NAV records for mutual fund schemes.

### 3. Scheme Performance

Fund-level performance information including:

* Returns
* Expense Ratios
* AUM

### 4. Investor Transactions

Transaction-level investment data including:

* SIP
* Lumpsum
* Redemption
* State
* Age Group
* City Tier

### 5. Portfolio Holdings

Portfolio allocation and sector exposure data.

### 6. Benchmark Indices

Historical benchmark market data including:

* NIFTY 50
* NIFTY 100

---

## ETL Pipeline

### Extraction

Data was collected from structured CSV datasets.

### Transformation

Data cleaning included:

* Null value handling
* Data type standardization
* Date formatting
* Duplicate removal
* Column normalization
* Validation checks

### Loading

Cleaned datasets were loaded into a SQLite database for analytical processing.

---

## Database Design

Database: `bluestock_mf.db`

Key entities:

* fund_master
* nav_history
* scheme_performance
* investor_transactions
* portfolio_holdings
* benchmark_indices

Relationships were established using:

* amfi_code
* date fields

---

## Performance Analytics

The project includes advanced mutual fund analytics.

### Daily Returns

daily_return = (NAVt / NAVt-1) − 1

### CAGR

CAGR = (Ending NAV / Beginning NAV)^(1/n) − 1

### Sharpe Ratio

Sharpe Ratio = (Rp − Rf) / σ × √252

Risk-Free Rate Assumption:

* 6.5%

### Sortino Ratio

Uses downside deviation instead of total volatility.

### Alpha & Beta

Calculated against benchmark returns using regression analysis.

### Maximum Drawdown

Measures peak-to-trough portfolio decline.

### Fund Scorecard

Composite scoring model based on:

* CAGR
* Sharpe Ratio
* Alpha
* Expense Ratio
* Maximum Drawdown

---

## Power BI Dashboard

### Page 1 — Industry Overview

Key Metrics:

* Total AUM
* SIP Inflows
* Folios
* Schemes

Visuals:

* Industry AUM Trend
* AUM by AMC
* KPI Cards

---

### Page 2 — Fund Performance

Visuals:

* Risk vs Return Scatter Plot
* Fund Scorecard
* Top Sharpe Ratio Funds

Features:

* Interactive filtering
* Performance ranking

---

### Page 3 — Investor Analytics

Visuals:

* State-wise Investment Analysis
* Investment Mode Distribution
* Age Group Analysis
* T30 vs B30 Analysis
* Monthly Transaction Trends

Insights:

* Investor demographics
* Geographic participation
* Investment behavior patterns

---

### Page 4 — SIP & Market Trends

Visuals:

* SIP Inflows vs NIFTY50 Market Trend
* SIP vs Lumpsum Contribution Trend
* Category-wise Investment Analysis

Insights:

* Market participation trends
* Investor sentiment analysis
* Category allocation patterns

---

### Page 5 — Fund Detail (Drill-Through)

Features:

* Fund-specific NAV Trend
* CAGR
* Sharpe Ratio
* Alpha
* Maximum Drawdown

Allows detailed analysis of individual mutual fund schemes.

---

## Key Insights

* Risk-adjusted returns vary significantly across fund categories.
* Equity-oriented schemes exhibit higher return potential with increased volatility.
* SIP investment behavior remains relatively resilient during market fluctuations.
* Investment activity is concentrated in major states and urban regions.
* Category allocation trends highlight investor preference toward growth-oriented funds.

---

## Repository Structure

project/

├── data/

│   ├── raw/

│   └── cleaned/

├── notebooks/

│   ├── ETL_Pipeline.ipynb

│   ├── EDA_Analysis.ipynb

│   └── Performance_Analytics.ipynb

├── database/

│   └── schemas.sql
│   └──queries.sql

├── dashboards/

│   └── bluestock_mf_dashboard.pbix

├── reports/

│   ├── Dashboard.pdf

├── README.md

└── requirements.txt

---

## Confidentiality Notice

The SQLite database file and large analytical outputs are excluded from version control to maintain repository size, portability, and data governance standards.

The repository contains only project code, documentation, and reproducible workflows.

---

## Author

Abdul Rehman Ansari

B.Sc. Information Technology

Data Analytics | Business Intelligence | Python | SQL | Power BI
