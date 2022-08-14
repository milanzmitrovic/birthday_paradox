

import pandas as pd
import plotly.express as px


def bar_chart_grouped(
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        color: str,
        barmode: str = 'group'
):

    # Aggregating data before plotting
    dff = df[[
        x_axis, y_axis, color
    ]].groupby(
        by=[x_axis, color],
        as_index=False
    ).sum()

    # Creating figure
    fig = px.histogram(
        dff,
        x=x_axis,
        y=y_axis,
        color=color,
        barmode=barmode,
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title=y_axis,
        xaxis_title=x_axis
    )
    return fig


if __name__ == '__main__':
    # df = pd.read_table(
    #     'https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv',
    #     decimal=','
    # )
    df = pd.read_csv('data_folder/super_store_data.csv', decimal=',')

    bar_chart_grouped(
        df=df,
        x_axis='Segment',
        y_axis='Profit',
        color='Ship Mode'
    ).show()


