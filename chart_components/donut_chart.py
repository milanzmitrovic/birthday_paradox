
import plotly.graph_objects as go
import pandas as pd


def donut_chart(
        df: pd.DataFrame,
        labels: str,
        values: str,
        hole_size: float,
        title: str
):
    # Aggregating data
    dff = df[[
        labels, values
    ]].groupby(
        by=[labels],
        as_index=False
    ).sum()

    # Creating figure
    fig = go.Figure(
        data=[go.Pie(
            labels=dff[labels],
            values=dff[values],
            hole=hole_size,
            title=title
        )
        ]
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title='1111',
        xaxis_title='222'
    )

    return fig


if __name__ == '__main__':
    # df = pd.read_table(
    #     'https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv',
    #     decimal=','
    # )
    df = pd.read_csv('data_folder/super_store_data.csv', decimal=',')

    donut_chart(
        df=df,
        labels='Ship Mode',
        values='Profit',
        hole_size=0.6,
        title='Test Chart Pie'
    ).show()

