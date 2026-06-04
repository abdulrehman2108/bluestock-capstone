-- 1 Which funds manage highest assets?
-- here the fact_aum and dim_fund table is used 
select a.scheme_name as scheme ,b.aum_crore as aum 
from dim_fund a 
join fact_aum b 
on a.amfi_code = b.amfi_code 
order by aum desc
limit 5;


-- 2 How does NAV trend monthly?
-- for personal understanding here no join only fact_nav table is used

select 
year(nav_date) as year,
month(nav_date) as month,
avg(nav) as avg_nav
from fact_nav
group by year,month
order by year,month;

-- 3 How are SIP investments growing yearly?
-- here fact_transactions is used 

select 
year(transaction_date) as year,
sum(amount_inr) as total_sip_amount
from fact_transactions 
where transaction_type = 'SIP'
group by year
order by year;


-- 4 Which states have highest investment activity?
select state,count(*) as total_transactions
from fact_transactions
group by state
order by total_transactions desc;


-- 5 Which funds are low cost?
SELECT
    d.scheme_name,
    p.expense_ratio_pct
FROM fact_performance p
JOIN dim_fund d
    ON p.amfi_code = d.amfi_code
WHERE p.expense_ratio_pct < 1
ORDER BY p.expense_ratio_pct;

-- 6 Which funds delivered highest long-term returns?

SELECT a.scheme_name,
	b.return_5yr_pct
FROM fact_performance b
JOIN dim_fund a 
ON a.amfi_code=b.amfi_code
ORDER BY b.return_5yr_pct DESC
LIMIT 10;

-- 7 Which funds have highest volatility?

select a.std_dev_ann_pct as std,
b.scheme_name as scheme 
from fact_performance a
join dim_fund b 
on a.amfi_code = b.amfi_code
order by std desc
limit 10; 

-- 8 How investment behaviour differs by geography?


SELECT 
    city_tier, AVG(amount_inr) AS avg_transaction
FROM
    fact_transactions
GROUP BY city_tier
ORDER BY avg_transaction DESC;


-- 9 Which categories dominate market?

SELECT category, COUNT(*) as total_funds
FROM dim_fund
GROUP BY category 
ORDER BY total_funds DESC;

-- 10 Which funds provide best return per unit risk?

SELECT b.scheme_name scheme,
a.sharpe_ratio sharp
FROM fact_performance a
JOIN dim_fund b 
ON a.amfi_code = b.amfi_code
ORDER BY sharp desc
LIMIT 10;


