
-- Number of sales by day of the week
SELECT 
dat.day_of_week,
count(DISTINCT transaction_id) as sales_count
FROM transactions t
LEFT JOIN dim_date dat ON t.transaction_date=dat.date
GROUP BY dat.day_of_week
ORDER BY sales_count DESC;

-- Total spending by day of the week
SELECT 
dat.day_of_week,
sum(quantity*price_per_unit) as total_spent
FROM transactions t
LEFT JOIN dim_date dat ON t.transaction_date=dat.date
GROUP BY dat.day_of_week
ORDER BY total_spent DESC;

-- Number of sales and total spending by category
SELECT
p.category,
count(DISTINCT transaction_id) as sales_count,
sum(t.quantity*t.price_per_unit) as total_spent
FROM transactions t
LEFT JOIN products p ON p.item=t.item
GROUP BY p.category
ORDER BY total_spent DESC;

-- 5 most expensive items
SELECT 
item_number,
price_per_unit
FROM products 
ORDER BY price_per_unit DESC
limit 5;

-- Item that generates the highest total spending
SELECT
item,
sum(quantity*price_per_unit) as total_spent
FROM transactions
GROUP by item
ORDER by total_spent DESC 
limit 1;

-- Are most transactions online or in store? 
SELECT
    location,
    count(DISTINCT transaction_id) as sales_count
FROM transactions 
GROUP by location
ORDER by sales_count DESC;

-- Are most online transactions made on the weekend?
SELECT
    weekend,
    location,
    count(DISTINCT transaction_id) as sales_count
FROM transactions t
LEFT JOIN dim_date dat ON dat.date=t.transaction_date
where location= 'Online'
GROUP by location,weekend
ORDER BY sales_count DESC;

-- What's the top payment method used?
SELECT
    payment_method,
    count(DISTINCT transaction_id) as sales_count
from transactions
GROUP BY payment_method
ORDER BY sales_count DESC
LIMIT 1;

-- Do clients spend more money using digital wallet and credit card than cash?
SELECT
payment_method,
sum(quantity*price_per_unit) as total_spent
FROM transactions
GROUP BY payment_method
ORDER by total_spent DESC;

-- Most profitable year/quarter

-- What percentage of each customer’s total spending 
-- is represented by their single largest purchase 
-- compared to their overall accumulated spending?

    WITH first_table as (
    SELECT
    customer_id,
    transaction_id,
    sum(quantity*price_per_unit) as transaction_spent
    FROM transactions
    GROUP BY customer_id,transaction_id  
), max_spent_per_tr as (
    SELECT
    ft.customer_id,
    max(ft.transaction_spent) as max_tr_spent,
    sum(ft.transaction_spent) as total_spent
    FROM first_table ft
    GROUP BY ft.customer_id
)   SELECT
    customer_id,
    CAST((max_tr_spent/total_spent*100) as decimal (5,2)) as perc_max_over_total
    FROM max_spent_per_tr
    ORDER BY customer_id;