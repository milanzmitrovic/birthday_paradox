
import pandas as pd
import plotly.express as px


# df = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv')
df = pd.read_csv('data_folder/super_store_data.csv', decimal=',')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])




df.columns

# Metrics: count(order date), sales, quantity, discount, profit, shipping cost
# Dimensions: order date, ship date,
# ship mode, segment, city, state, country, market,
# region, category, sub-category, product name


