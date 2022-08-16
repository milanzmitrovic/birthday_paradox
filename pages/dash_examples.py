
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback


def dash_example():

    return dmc.Container([

        dmc.Space(h=40),

        html.H2('Open source library'),

        html.Li('There is Dash open source (free for anyone) and Dash Enterprise.'),

        html.Br(),

        html.Li('Dash Enterprise provide platform for running Dash apps'),

        dmc.Space(h=40),

        html.H2('Main Dash Components:'),

        html.Li('Layout'),

        html.Br(),

        html.Li(
            'Describing layout of app - similar to HTML syntax',
            style={'margin-left': 30}
        ),
        html.Br(),

        html.Li('Callbacks'),

        html.Br(),

        html.Li(
            'Defining functionality of app',
            style={'margin-left': 30}
        ),

        html.Br(),

        html.Li(
            'Everything is based on Input/Output basis',
            style={'margin-left': 30}
        ),

        html.Br(),

        dmc.Space(h=40),

        html.H2("Dash started as 'Shiny for Python'"),

        html.Li('It is entire web framework, not only dashboarding tool!'),

        dmc.Space(h=40),

        html.H2("Today, it is 'React for Python'"),

        html.Li('You can wrap any React library into Dash and create your custom Dash components'),

        dmc.Space(h=40),

        html.H2('The best tool to build dashboards'),

        html.Li('My personal experience - It is way more intuitive than GUI tools such as Tableau and PowerBI'),

        dmc.Space(h=40),

        html.H2('Everything is possible'),

        html.Li("You will never say 'Not possible' to your client/manager"),

        dmc.Space(h=40),

        html.H2('Example'),

        html.Li([
            html.A("Link to example", href='https://gist.github.com/milanzmitrovic/134bfc31a3a9540bf2b4f14ceeac56f9',
                   target="_blank")
        ]),

        dmc.Space(h=60)

    ])


