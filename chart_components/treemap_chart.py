
import pandas as pd
import plotly.express as px


def treemap_chart(
        df: pd.DataFrame,
        dimensions: list,
        metric: str
):

    dff = df[
        dimensions + [metric]
    ].groupby(
        by=dimensions,
        as_index=False
    ).sum()

    fig = px.treemap(
        dff,
        path=[px.Constant("all")] + dimensions,
        values=metric
    )

    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.update_traces(root_color="lightgrey")

    return fig


if __name__ == '__main__':
    # df = pd.read_table(
    #     'https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv',
    #     decimal=','
    # )
    df = pd.read_csv('data_folder/super_store_data.csv', decimal=',')

    treemap_chart(
        df=df,
        dimensions=['Ship Mode', 'Segment', 'Shipping Cost', 'Category', 'Sub-Category'],
        metric='Sales'
    ).show()

