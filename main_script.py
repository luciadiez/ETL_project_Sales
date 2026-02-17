#%%
# Load data
import pandas as pd
import numpy as np
df=pd.read_csv('data/retail_store_sales.csv')

#%%
#print(df.dtypes)

df['Item'].unique()

df['Item'].value_counts()

#Check for duplicates
duplicates_id=df[df.duplicated('Transaction ID', keep=False)]

# %%
# Create a table with unique values for item and price per unit
items_cost= df.drop_duplicates(subset=['Item','Price Per Unit'])[['Item','Price Per Unit']]
# split the items column in three
items_cost[['1','item_number','category_code']] = items_cost['Item'].str.split('_', expand=True)
# keep only one unique item numbers, remove NA and sort
items_cost = (
    items_cost
    .drop_duplicates(subset=['item_number', 'Price Per Unit'])
    [['item_number', 'Price Per Unit']]
    .dropna()
    .sort_values(by='item_number')
    .pipe(lambda df: df.assign(item_number = df['item_number'].astype(int)))
)

# to remove a string from values
#items_cost['Item']= items_cost['Item'].str.strip('Item')





# %%
