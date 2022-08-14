
import plotly.express as px
import pandas as pd
import dash_mantine_components as dmc
from dash import dcc


def line_chart(
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        color: str = None
):

    dff = df.sort_values(by=x_axis)

    fig = px.line(
        data_frame=dff,
        x=x_axis,
        y=y_axis,
        color=color,
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title='Price',
        xaxis_title='Date'
    )

    return dmc.Paper([
        dcc.Graph(
            figure=fig
        )],
        withBorder=True,
        radius='lg',
        shadow='xl'
    )


# Always group by before plotting!!!
# df = px.data.gapminder().query("continent=='Oceania'")
#
# line_chart(df=df, x_axis='year', y_axis='lifeExp').show()
#
# dff = df[['year', 'country', 'lifeExp']].groupby(by=['year', 'country'], as_index=False).mean()
#
# line_chart(df=dff, x_axis='year', y_axis='lifeExp').show()
# line_chart(df=dff, x_axis='year', y_axis='lifeExp', color='country').show()
#
