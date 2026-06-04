create database bluestock_mf;

use bluestock_mf;

create table dim_fund(
amfi_code int PRIMARY KEY,

scheme_name varchar(255),

fund_house varchar(100),

category varchar(100),

plan varchar(50),

risk_grade varchar(50)


);

create table dim_date(


date_id int auto_increment primary key,

full_date date unique,

day int,

month int,

quarter int,

year int,

weekday_name varchar(20)


);

CREATE TABLE fact_nav (

    nav_id INT AUTO_INCREMENT PRIMARY KEY,

    amfi_code INT,

    nav_date DATE,

    nav DECIMAL(10,4),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);




CREATE TABLE fact_transactions (

    transaction_id INT AUTO_INCREMENT PRIMARY KEY,

    investor_id VARCHAR(50),

    amfi_code INT,

    transaction_date DATE,

    transaction_type VARCHAR(50),

    amount_inr DECIMAL(15,2),

    state VARCHAR(100),

    city VARCHAR(100),

    city_tier VARCHAR(50),

    age_group VARCHAR(50),

    gender VARCHAR(20),

    annual_income DECIMAL(15,2),

    payment_method VARCHAR(50),

    kyc_status VARCHAR(50),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);


CREATE TABLE fact_performance (

    performance_id INT AUTO_INCREMENT PRIMARY KEY,

    amfi_code INT,

    return_1yr_pct DECIMAL(10,2),

    return_3yr_pct DECIMAL(10,2),

    return_5yr_pct DECIMAL(10,2),

    benchmark_3yr_pct DECIMAL(10,2),

    alpha DECIMAL(10,2),

    beta DECIMAL(10,2),

    sharpe_ratio DECIMAL(10,2),

    sortino_ratio DECIMAL(10,2),

    std_dev_ann_pct DECIMAL(10,2),

    max_drawdown_pct DECIMAL(10,2),

    expense_ratio_pct DECIMAL(10,2),

    morningstar_rating INT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);


CREATE TABLE fact_aum (

    aum_id INT AUTO_INCREMENT PRIMARY KEY,

    amfi_code INT,

    aum_crore DECIMAL(15,2),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);


