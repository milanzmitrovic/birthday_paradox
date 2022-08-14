import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback


def intro():
    return dmc.Container([

        dmc.Space(h=30),

        dmc.SimpleGrid(
            children=[
                dmc.Image(
                    src="assets/birthday_paradox_img.jpeg",
                    alt="Birthday Paradox",
                    withPlaceholder=False
                ),
                dmc.Image(
                    src="assets/Plotly_Dash_logo.png",
                    alt="Plotly-Dash",
                    withPlaceholder=False
                )

            ],
            cols=2,
            breakpoints=[
                {"maxWidth": 755, "cols": 2, "spacing": "sm"},
                {"maxWidth": 600, "cols": 1, "spacing": "sm"},
            ]
        ),

        dmc.Space(h=30),

        html.H1('Presentation Structure'),
        html.Br(),

        html.H5('Part 1'),
        html.Hr(),
        html.Hr(),

        html.H3('What is birthday paradox definition?'),
        html.Br(),
        html.H3("Why is this statement called 'Paradox'?"),
        html.Br(),
        html.H3('How to numerically develope/proove Birthday paradox?'),
        html.Br(),
        html.H3('Why is this topic interesting/important for us? What can we learn from it?'),

        html.Br(),

        html.H5('Part 2'),
        html.Hr(),
        html.Hr(),

        html.H3('What is Plotly?'),
        html.Br(),
        html.H3('What is Python Dash framework?'),

        html.Br(),
        html.H3('How to become full stack data developer?'),

        dmc.Space(h=60),

    ])


