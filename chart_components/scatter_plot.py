




import plotly.express as px
import pandas as pd


def scatter_plot(
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        color: str = None,
        size: str = None,
        hover_data: list = None
):
    fig = px.scatter(
        data_frame=df,
        x=x_axis,
        y=y_axis,
        color=color,
        size=size,
        hover_data=hover_data,
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title=y_axis,
        xaxis_title=x_axis
    )

    return fig


# df = px.data.iris()
#
# scatter_plot(df=df,
#              x_axis="sepal_width",
#              y_axis="sepal_length",
#              # color="species",
#              # size='petal_length',
#              # hover_data=['petal_width']
#              ).show()


