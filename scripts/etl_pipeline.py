from sqlalchemy import create_engine
import pandas as pd



engine = create_engine(
    "mysql+pymysql://root:root@localhost/bluestock_mf"
)

print("MYSQL connection successful")



dim_fund = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/fund_master_cleaned.csv"
)

date_df = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/dim_date.csv"
)

fact_nav = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/fact_nav.csv"
)

fact_transactions = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/fact_transactions.csv"
)

fact_performance = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/fact_performance.csv"
)

fact_aum = pd.read_csv(
    "C:/Users/abdul/OneDrive/Desktop/Bluestock_capstone/data/processed/fact_aum.csv"
)

print("Processed datasets loaded")


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


print("\n========== ROW COUNTS ==========")

print("dim_fund:", len(dim_fund))
print("dim_date:", len(date_df))
print("fact_nav:", len(fact_nav))
print("fact_transactions:", len(fact_transactions))
print("fact_performance:", len(fact_performance))
print("fact_aum:", len(fact_aum))

print("\nETL pipeline completed successfully")