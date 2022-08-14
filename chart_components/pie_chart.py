
import pandas as pd
import plotly.express as px


def pie_chart(
        df: pd.DataFrame,
        labels: str,
        values: str,
        title: str
):
    dff = df[[
        labels,
        values
    ]].groupby(
        by=[labels],
        as_index=False
    ).sum()

    fig = px.pie(
        df,
        values=dff[values],
        names=dff[labels],
        title=title)

    return fig


if __name__ == '__main__':
    # df = pd.read_table(
    #     'https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv',
    #     decimal=','
    # )
    df = pd.read_csv('data_folder/super_store_data.csv', decimal=',')

    pie_chart(
        df=df,
        labels='Ship Mode',
        values='Profit',
        title='Test Pie Chart 1'
    ).show()

