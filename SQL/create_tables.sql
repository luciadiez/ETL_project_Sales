-- #  Create products table
CREATE TABLE IF NOT EXISTS products (
    item_id INT NOT NULL,
    item VARCHAR(50),
    category VARCHAR(50),
    category_code VARCHAR(5),
    price_per_unit FLOAT,
    PRIMARY KEY (item_id)
);

INSERT INTO products (
    item_id,
    item,
    category,
    price_per_unit
)
    SELECT distinct 
            CAST(SUBSTRING(item FROM '_([^_]+)_') AS INT) AS item_id,
            item,
            category,
            SUBSTRING(item FROM '[^_]+$') as category_code,
            price_per_unit
    FROM sales;

-- # Create customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(50) NOT NULL,
    PRIMARY KEY (customer_id)
);

INSERT INTO customers(
    customer_id
)
    SELECT distinct customer_id
    FROM sales;

-- # Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR NOT NULL,
    item_id VARCHAR(255),
    customer_id VARCHAR(50),
    payment_method VARCHAR(50),
    location VARCHAR(255),
    transaction_date DATE,
    discount_applied  BOOLEAN,
    quantity INT,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (item_id) REFERENCES products9(item_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO transactions (
    transaction_id,
            item_id,
            customer_id,
            payment_method,
            location,
            transaction_date,
            discount_applied,
            quantity
)
    SELECT distinct transaction_id,
            CAST(SUBSTRING(item FROM '_([^_]+)_') AS INT) as item_id,
            customer_id,
            payment_method,
            location,
            transaction_date,
            discount_applied,
            quantity
    FROM sales;








