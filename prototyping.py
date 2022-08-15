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


df = pd.read_csv(
    'https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv')

df2 = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv')

df.to_csv(r'data_folder/us_births_1994-2003.csv')

df2.to_csv(r'data_folder/us_births_00-14.csv')

df_derived = df.groupby(by=['month', 'date_of_month'], as_index=False).sum()


fig = px.scatter(
    data_frame=df_derived,
    x='date_of_month',
    y='month',
    color='births',
    template='simple_white',
    symbol_sequence=['square'],
    size=[5] * len(df_derived)
)

fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

fig.update_traces(marker={'size': 30})

fig.show()

