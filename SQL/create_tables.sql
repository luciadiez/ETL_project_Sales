-- #  Create products table
CREATE TABLE IF NOT EXISTS products (
    item_number INT NOT NULL,
    item VARCHAR(50),
    category VARCHAR(50),
    category_code VARCHAR(5),
    price_per_unit FLOAT,
    PRIMARY KEY (item)
);

INSERT INTO products (
    item_number,
    item,
    category,
    category_code,
    price_per_unit
)
    SELECT distinct 
            item_number,
            item,
            category,
            category_code,
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
    item VARCHAR(255),
    customer_id VARCHAR(50),
    payment_method VARCHAR(50),
    location VARCHAR(255),
    transaction_date DATE,
    discount_applied  BOOLEAN,
    quantity INT,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (item) REFERENCES products(item),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO transactions (
            transaction_id,
            item,
            customer_id,
            payment_method,
            location,
            transaction_date,
            discount_applied,
            quantity
)
    SELECT distinct transaction_id,
            item,
            customer_id,
            payment_method,
            location,
            transaction_date,
            discount_applied,
            quantity
    FROM sales;




