#%%

import pandas as pd
import numpy as np
# Load data
df=pd.read_csv('data/retail_store_sales.csv')

#%% Exploring the data

columns = df.columns
df.describe(include='object')

df['Item'].value_counts()
df['Category'].value_counts()
df['Payment Method'].value_counts()
df['Location'].value_counts()

#Check for duplicates
duplicates_id=df[df.duplicated('Transaction ID', keep=False)]
duplicates_customer=df[df.duplicated('Customer ID', keep=False)]

#%% Populate 'Quantity' and 'Total Spent'

df['Quantity']= np.where(
    df['Quantity'].isna(),
    df['Total Spent']/df['Price Per Unit'],
    df['Quantity']
)

df['Total Spent']= np.where(
    df['Total Spent'].isna(),
    df['Quantity']*df['Price Per Unit'],
    df['Total Spent']
)

# Change 'Transaction date' to date

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Replace NA in 'Discount applied' by 'Unknown'
df['Discount Applied']= np.where(
    df['Discount Applied'].isna(),
    'Unknown',
    df['Discount Applied']
)

# %% Create a reference table for items and prices
items_cost =df
# split the items column in three
items_cost[['1','item_number','category_code']] = items_cost['Item'].str.split('_', expand=True)

# check that all items with same number are priced the same
# there should only be one unique value for price per item
items_cost.groupby('item_number')['Price Per Unit'].nunique().max() ==1

# Create a table with unique values for item and price per unit
items_cost= items_cost.drop_duplicates(subset=['item_number','Price Per Unit'])[['item_number','Price Per Unit']]

# keep only one unique item numbers, remove NA and sort
items_cost = (
    items_cost
    .drop_duplicates(subset=['item_number', 'Price Per Unit'])
    [['item_number', 'Price Per Unit']]
    .dropna()
    .pipe(lambda df: df.assign(item_number = df['item_number'].astype(int)))
    .sort_values('item_number')
)
# # Add a column identifying items by number only
# df['item_number']= (
#     df['Item']
#     .str.split('_')
#     .str.get(1)
#     .astype('Int64')
# )

# %% Create reference table for categories

cat_table= df[['Category','Item']]
cat_table['cat_code']= (
    cat_table['Item']
    .str.split('_')
    .str.get(2)
)

cat_table= (
    cat_table
    .drop_duplicates(subset=['Category','cat_code'])
    .dropna()
    [['Category','cat_code']]
)

# %%

# Merge df with the ref table for items to create a new column with no missing values for item (item_number)
df = pd.merge(df,items_cost, on='Price Per Unit')
df= pd.merge(df,cat_table, on= 'Category')

# Fill Item column

df['Item'] = np.where(
    df['Item'].isna(),
    'Item_'+df['item_number_y'].astype(str)+ '_'+ df['cat_code'],
    df['Item']
)

# Leave original columns only
df = df[columns]


