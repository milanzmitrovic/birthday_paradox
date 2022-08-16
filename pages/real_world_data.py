
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import pandas as pd

from chart_components.scatter_plot_with_squares import scatter_plot_with_squares


def real_world_data(
        df: pd.DataFrame
):
    return dmc.Container([

        dmc.Space(h=40),

        scatter_plot_with_squares(df=df),

        dmc.Space(h=60),

        html.Li([
            html.A(
                "Link to dataset",
                href='https://github.com/fivethirtyeight/data/blob/master/births/US_births_2000-2014_SSA.csv',
                target="_blank")
        ], style={'textAlign': 'center'}),

        dmc.Space(h=70),


    ], fluid=True)

