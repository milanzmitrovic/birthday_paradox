
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import pandas as pd


from pages.intro import intro
from pages.paradox_description import paradox_description
from pages.plotly_tab import plotly_tab
from pages.tab_2 import tab_2
from pages.paradox_example import create_layout
from pages.tab_4 import tab_4

app = Dash(__name__)

df = pd.read_table(
    'https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv',
    decimal=','
)

app.layout = html.Div([
    html.H1('Birthday Paradox & Intro to Dash-Plotly', style={'textAlign': 'center'}),

    dcc.Tabs(
        id="tabs-example-graph",
        value='intro',
        children=[
            dcc.Tab(label='Intro', value='intro'),

            dcc.Tab(label='Paradox - Description', value='paradox-description'),
            dcc.Tab(label='Paradox - Numerical approach', value='numerical_approach'),
            dcc.Tab(label='Paradox - Analytical approach', value='analytical_approach'),
            dcc.Tab(label='Paradox - Example', value='tab-example'),
            dcc.Tab(label='Real world data - US births', value='tab-example1'),

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

    elif tab == 'numerical_approach':
        return tab_2()

    elif tab == 'tab-example':
        return create_layout()

    elif tab == 'tab-example1':
        return tab_4()

    elif tab == 'dash-examples':
        return tab_4()

    elif tab == 'plotly-examples':
        return plotly_tab(df=df)

    elif tab == 'paradox-description':
        return paradox_description()


if __name__ == '__main__':
    app.run_server(debug=False)


