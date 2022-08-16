
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import pandas as pd

from pages.analytical_approach import analytical_approach
from pages.dash_examples import dash_example
from pages.intro import intro
from pages.numerical_approach import numerical_approach
from pages.paradox_description import paradox_description
from pages.plotly_tab import plotly_tab
from pages.tab_2 import tab_2
from pages.paradox_example import create_layout
from pages.real_world_data import real_world_data

app = Dash(__name__)

df = pd.read_table(
    'https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv',
    decimal=','
)

df_births = pd.read_csv('data_folder/us_births_00-14.csv')

app.layout = html.Div([

    dmc.Header(
        height=60,
        children=[
            html.H1("Birthday Paradox & Intro to Dash-Plotly"),
        ],
        style={
            "backgroundColor": "#03a1fc",
            'textAlign': 'center'
        }
    ),

    dmc.Space(h=20),

    # html.H1('Birthday Paradox & Intro to Dash-Plotly', style={'textAlign': 'center'}),

    dcc.Tabs(
        id="tabs-example-graph",
        value='intro',
        children=[
            dcc.Tab(label='Intro', value='intro'),

            dcc.Tab(label='Paradox - Description', value='paradox-description'),

            dcc.Tab(label='Paradox - Numerical approach', value='numerical_approach'),
            dcc.Tab(label='Paradox - Analytical approach', value='analytical_approach'),

            dcc.Tab(label='Paradox - Example', value='paradox-example'),

            dcc.Tab(label='Real world data - US births', value='real-world-data'),

            dcc.Tab(label='Plotly', value='plotly-examples'),
            dcc.Tab(label='Dash', value='dash-examples')

        ]
    ),

    html.Div(id='tabs-content-example-graph')
])


@callback(
    Output('tabs-content-example-graph', 'children'),
    Input('tabs-example-graph', 'value')
)
def render_content(tab):

    if tab == 'tab-1-example-graph':
        pass

    elif tab == 'intro':
        return intro()

    elif tab == 'paradox-description':
        return paradox_description()

    elif tab == 'numerical_approach':
        return numerical_approach()

    elif tab == 'paradox-example':
        return create_layout()

    elif tab == 'real-world-data':
        return real_world_data(df=df_births)

    elif tab == 'dash-examples':
        return dash_example()

    elif tab == 'plotly-examples':
        return plotly_tab(df=df)

    elif tab == 'analytical_approach':
        return analytical_approach()


if __name__ == '__main__':
    app.run_server(debug=False)


