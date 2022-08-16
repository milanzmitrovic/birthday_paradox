
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
from dash import html, dcc


def scatter_plot_with_squares(
        df: pd.DataFrame
):
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
        margin=dict(t=50, l=25, r=25, b=25),
        xaxis_title='Day of Month',
        yaxis_title='Month',
        title='Chances to be born on particular day',
        title_font_size=15,
        title_x=0.5
    )

    fig.update_traces(marker={'size': 30})

    return dmc.Paper([
        html.H2('US births from 2000-2014', style={'textAlign': 'center'}),

        dcc.Graph(figure=fig)

    ])

