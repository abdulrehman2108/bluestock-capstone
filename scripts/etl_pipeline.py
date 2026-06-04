from sqlalchemy import create_engine
import pandas as pd


engine = create_engine(
    "mysql+pymysql://root:root@localhost/bluestock_mf"
)


print("MYSQL connection successful")



fund_df = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/fund_master_cleaned.csv"
)

nav_df = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/nav_history_cleaned.csv"
)

txn_df = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/investor_transactions_cleaned.csv"
)

perf_df = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/scheme_performance_cleaned.csv"
)

print("CSV files loaded successfully")



nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    errors="coerce"
)

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"],
    errors="coerce"
)



fund_df = fund_df.rename(
    columns={
        "risk_category": "risk_grade"
    }
)


dim_fund = fund_df[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan",
        "risk_grade"
    ]
].copy()

# Remove null PKs
dim_fund = dim_fund[
    dim_fund["amfi_code"].notnull()
]

# Remove duplicates
dim_fund = dim_fund.drop_duplicates(
    subset=["amfi_code"]
)

# Reset index
dim_fund = dim_fund.reset_index(drop=True)

print("dim_fund cleaned")


date_df = pd.DataFrame()

date_df["full_date"] = nav_df["date"]

# Remove null dates
date_df = date_df[
    date_df["full_date"].notnull()
]

# Remove duplicates
date_df = date_df.drop_duplicates(
    subset=["full_date"]
)

# Reset index
date_df = date_df.reset_index(drop=True)

# Generate attributes
date_df["day"] = (
    date_df["full_date"].dt.day
)

date_df["month"] = (
    date_df["full_date"].dt.month
)

date_df["quarter"] = (
    date_df["full_date"].dt.quarter
)

date_df["year"] = (
    date_df["full_date"].dt.year
)

date_df["weekday_name"] = (
    date_df["full_date"].dt.day_name()
)

print("dim_date cleaned")


fact_nav = nav_df[
    [
        "amfi_code",
        "date",
        "nav"
    ]
].copy()

fact_nav = fact_nav.rename(
    columns={"date": "nav_date"}
)

# Remove nulls
fact_nav = fact_nav[
    fact_nav["amfi_code"].notnull()
]

fact_nav = fact_nav[
    fact_nav["nav_date"].notnull()
]

# Remove duplicates
fact_nav = fact_nav.drop_duplicates(
    subset=["amfi_code", "nav_date"]
)

fact_nav = fact_nav.reset_index(drop=True)

print("fact_nav cleaned")


fact_transactions = txn_df[
    [
        "investor_id",
        "amfi_code",
        "transaction_date",
        "transaction_type",
        "amount_inr",
        "state",
        "city",
        "city_tier",
        "age_group",
        "gender",
        "annual_income_lakh",
        "payment_mode",
        "kyc_status"
    ]
].copy()

# Remove null PK/FK values
fact_transactions = fact_transactions[
    fact_transactions["amfi_code"].notnull()
]

fact_transactions = fact_transactions[
    fact_transactions["transaction_date"].notnull()
]

# Remove duplicates
fact_transactions = fact_transactions.drop_duplicates()

fact_transactions = fact_transactions.reset_index(drop=True)

print("fact_transactions cleaned")


fact_performance = perf_df[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "expense_ratio_pct",
        "morningstar_rating"
    ]
].copy()

# Remove null PK/FK values
fact_performance = fact_performance[
    fact_performance["amfi_code"].notnull()
]

# Remove duplicates
fact_performance = fact_performance.drop_duplicates(
    subset=["amfi_code"]
)

fact_performance = fact_performance.reset_index(drop=True)

print("fact_performance cleaned")



fact_aum = perf_df[
    [
        "amfi_code",
        "aum_crore"
    ]
].copy()

fact_aum = fact_aum[
    fact_aum["amfi_code"].notnull()
]

fact_aum = fact_aum.drop_duplicates(
    subset=["amfi_code"]
)

fact_aum = fact_aum.reset_index(drop=True)

print("fact_aum cleaned")



with engine.begin() as conn:

    conn.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

    conn.execute(text("TRUNCATE TABLE fact_nav"))
    conn.execute(text("TRUNCATE TABLE fact_transactions"))
    conn.execute(text("TRUNCATE TABLE fact_performance"))
    conn.execute(text("TRUNCATE TABLE fact_aum"))
    conn.execute(text("TRUNCATE TABLE dim_date"))
    conn.execute(text("TRUNCATE TABLE dim_fund"))

    conn.execute(text("SET FOREIGN_KEY_CHECKS = 1"))

print("Old warehouse data cleared")



dim_fund.to_sql(
    "dim_fund",
    con=engine,
    if_exists="append",
    index=False
)

date_df.to_sql(
    "dim_date",
    con=engine,
    if_exists="append",
    index=False
)

print("Dimension tables loaded")



fact_nav.to_sql(
    "fact_nav",
    con=engine,
    if_exists="append",
    index=False
)

fact_transactions.to_sql(
    "fact_transactions",
    con=engine,
    if_exists="append",
    index=False
)

fact_performance.to_sql(
    "fact_performance",
    con=engine,
    if_exists="append",
    index=False
)

fact_aum.to_sql(
    "fact_aum",
    con=engine,
    if_exists="append",
    index=False
)

print("Fact tables loaded")





print("dim_fund:", len(dim_fund))
print("dim_date:", len(date_df))
print("fact_nav:", len(fact_nav))
print("fact_transactions:", len(fact_transactions))
print("fact_performance:", len(fact_performance))
print("fact_aum:", len(fact_aum))

print("\nETL pipeline completed successfully")

