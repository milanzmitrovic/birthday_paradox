
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback

from chart_components.analytical_prob_chart import generate_analytical_chart


def analytical_approach():

    return dmc.Container([

        dmc.Space(h=40),

        html.H2('Analytical approach:'),

        html.Li('count(number of cases we like) / count(number of all possible cases) * 100'),

        dmc.Space(h=40),

        html.H2('How it works?'),

        html.Li('We will use small trick :)'),

        html.Br(),

        html.Li('Instead of calculating probability of having of AT LEAST two matching birthdays, lets calculate probability of NOT having at least two birthdays.'),

        html.Br(),

        html.Li('[probability of having at least two birthdays] + [probability of NOT having at least two birthdays] = 1'),

        html.Br(),

        html.Li('So, [probability of having at least two birthdays] = 1 - [probability of NOT having at least two birthdays]'),

        dcc.Markdown('''


        ```python
    
        365/365 * 364/365 * 363/365 ...
    
        n = 365
        prob_of_not = 1
    
        for i in range(90):
    
            prob_of_not = prob_of_not * (n - i) / 365
    
            print(i, 'Probability of not having common birthdays', prob_of_not)
            print(i, 'Probability of having common birthdays', 1 - prob_of_not)
    
    ```'''),

        dmc.Space(h=30),


        dmc.Space(h=40),

        html.H2('Analytic VS Numeric approach'),

        html.Li('More intuitive?'),

        html.Br(),

        html.Li(
            'Numerical',
            style={'margin-left': 30}
        ),

        html.Br(),
        html.Br(),

        html.Li('More general?'),

        html.Br(),

        html.Li(
            'Numerical',
            style={'margin-left': 30}
        ),

        html.Br(),
        html.Br(),

        html.Li('Older?'),

        html.Br(),

        html.Li(
            'Analytical',
            style={'margin-left': 30}
        ),

        html.Br(),
        html.Br(),

        html.Li('More modern?'),

        html.Br(),

        html.Li(
            'Numerical',
            style={'margin-left': 30}
        ),

        html.Br(),
        html.Br(),

        html.Li('Computationally efficient?'),

        html.Br(),

        html.Li(
            'Analytical',
            style={'margin-left': 30}
        ),

        html.Br(),
        html.Br(),

        html.H2('Example'),

        html.Li([
            html.A("Link to example", href='https://gist.github.com/milanzmitrovic/134bfc31a3a9540bf2b4f14ceeac56f9',
                   target="_blank")
        ]),

        dmc.Space(h=60)



    ])



