# Bluestock Mutual Fund Analytics — Data Dictionary

## Project Overview

This project is a financial analytics data warehouse built using:

* Python
* Pandas
* MySQL
* SQLAlchemy

The warehouse is designed using a star schema architecture for mutual fund analytics, investor behavior analysis, NAV trend analysis, and fund performance reporting.

---

# Dimension Tables

## 1. dim_fund

Description:
Stores master metadata information for all mutual fund schemes.

| Column Name | Data Type    | Description                               | Source          |
| ----------- | ------------ | ----------------------------------------- | --------------- |
| amfi_code   | INT          | Unique AMFI scheme identifier             | fund_master.csv |
| scheme_name | VARCHAR(255) | Mutual fund scheme name                   | fund_master.csv |
| fund_house  | VARCHAR(100) | Asset management company name             | fund_master.csv |
| category    | VARCHAR(100) | Fund category (Equity, Debt, Hybrid etc.) | fund_master.csv |
| plan        | VARCHAR(50)  | Fund plan type (Direct/Regular)           | fund_master.csv |
| risk_grade  | VARCHAR(50)  | Risk classification of the fund           | fund_master.csv |

---

## 2. dim_date

Description:
Stores calendar and date-related attributes used for time-series analytics.

| Column Name  | Data Type   | Description           | Source          |
| ------------ | ----------- | --------------------- | --------------- |
| date_id      | INT         | Surrogate primary key | Generated       |
| full_date    | DATE        | Calendar date         | nav_history.csv |
| day          | INT         | Day of month          | Generated       |
| month        | INT         | Month number          | Generated       |
| quarter      | INT         | Quarter number        | Generated       |
| year         | INT         | Year                  | Generated       |
| weekday_name | VARCHAR(20) | Name of weekday       | Generated       |

---

# Fact Tables

## 3. fact_nav

Description:
Stores daily Net Asset Value (NAV) history for mutual fund schemes.

| Column Name | Data Type     | Description                   | Source          |
| ----------- | ------------- | ----------------------------- | --------------- |
| nav_id      | INT           | Primary key for NAV records   | Generated       |
| amfi_code   | INT           | Mutual fund scheme identifier | nav_history.csv |
| nav_date    | DATE          | NAV reporting date            | nav_history.csv |
| nav         | DECIMAL(10,4) | Daily NAV value               | nav_history.csv |

---

## 4. fact_transactions

Description:
Stores investor transaction activity including SIPs, lumpsum investments, and redemptions.

| Column Name      | Data Type     | Description                        | Source                    |
| ---------------- | ------------- | ---------------------------------- | ------------------------- |
| transaction_id   | INT           | Primary key for transactions       | Generated                 |
| investor_id      | VARCHAR(50)   | Unique investor identifier         | investor_transactions.csv |
| amfi_code        | INT           | Mutual fund scheme identifier      | investor_transactions.csv |
| transaction_date | DATE          | Date of transaction                | investor_transactions.csv |
| transaction_type | VARCHAR(50)   | SIP, Lumpsum, or Redemption        | investor_transactions.csv |
| amount_inr       | DECIMAL(15,2) | Transaction amount in INR          | investor_transactions.csv |
| state            | VARCHAR(100)  | Investor state                     | investor_transactions.csv |
| city             | VARCHAR(100)  | Investor city                      | investor_transactions.csv |
| city_tier        | VARCHAR(50)   | Tier classification of city        | investor_transactions.csv |
| age_group        | VARCHAR(50)   | Investor age category              | investor_transactions.csv |
| gender           | VARCHAR(20)   | Investor gender                    | investor_transactions.csv |
| annual_income    | DECIMAL(10,2) | Investor annual income in lakhs    | investor_transactions.csv |
| payment_method   | VARCHAR(50)   | Payment method used for investment | investor_transactions.csv |
| kyc_status       | VARCHAR(50)   | Investor KYC verification status   | investor_transactions.csv |

---

## 5. fact_performance

Description:
Stores performance and risk analytics metrics for mutual fund schemes.

| Column Name        | Data Type     | Description                           | Source                 |
| ------------------ | ------------- | ------------------------------------- | ---------------------- |
| performance_id     | INT           | Primary key for performance records   | Generated              |
| amfi_code          | INT           | Mutual fund scheme identifier         | scheme_performance.csv |
| return_1yr_pct     | DECIMAL(10,2) | 1-year return percentage              | scheme_performance.csv |
| return_3yr_pct     | DECIMAL(10,2) | 3-year return percentage              | scheme_performance.csv |
| return_5yr_pct     | DECIMAL(10,2) | 5-year return percentage              | scheme_performance.csv |
| benchmark_3yr_pct  | DECIMAL(10,2) | Benchmark 3-year return percentage    | scheme_performance.csv |
| alpha              | DECIMAL(10,2) | Risk-adjusted excess return metric    | scheme_performance.csv |
| beta               | DECIMAL(10,2) | Volatility relative to market         | scheme_performance.csv |
| sharpe_ratio       | DECIMAL(10,2) | Risk-adjusted performance metric      | scheme_performance.csv |
| sortino_ratio      | DECIMAL(10,2) | Downside risk-adjusted return metric  | scheme_performance.csv |
| std_dev_ann_pct    | DECIMAL(10,2) | Annualized standard deviation         | scheme_performance.csv |
| max_drawdown_pct   | DECIMAL(10,2) | Maximum historical decline percentage | scheme_performance.csv |
| expense_ratio_pct  | DECIMAL(10,2) | Fund expense ratio percentage         | scheme_performance.csv |
| morningstar_rating | INT           | Morningstar fund rating               | scheme_performance.csv |

---

## 6. fact_aum

Description:
Stores Assets Under Management (AUM) metrics for mutual fund schemes.

| Column Name | Data Type     | Description                                | Source                 |
| ----------- | ------------- | ------------------------------------------ | ---------------------- |
| aum_id      | INT           | Primary key for AUM records                | Generated              |
| amfi_code   | INT           | Mutual fund scheme identifier              | scheme_performance.csv |
| aum_crore   | DECIMAL(15,2) | Total assets under management in crore INR | scheme_performance.csv |

---

# Source References

| Source File               | Description                             |
| ------------------------- | --------------------------------------- |
| fund_master.csv           | Master metadata for mutual fund schemes |
| nav_history.csv           | Historical daily NAV data               |
| investor_transactions.csv | Investor transaction activity           |
| scheme_performance.csv    | Fund performance and analytics metrics  |

---

# Warehouse Architecture

The warehouse follows a star schema design:

* Dimension Tables:

  * dim_fund
  * dim_date

* Fact Tables:

  * fact_nav
  * fact_transactions
  * fact_performance
  * fact_aum

The schema is optimized for:

* financial analytics
* mutual fund reporting
* investor behavior analysis
* dashboarding
* BI queries
