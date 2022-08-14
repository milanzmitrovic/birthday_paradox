
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback


def tab_4():
    return html.Div([
        html.H1('Test'),
        html.H2('Test 2'),
        html.H3(['Test 3'])
    ])

