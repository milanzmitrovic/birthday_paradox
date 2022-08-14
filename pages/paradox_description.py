
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback


def paradox_description():
    return dmc.Container([

        dmc.Space(h=40),

        html.H1('Main question that should be answered'),

        html.Br(),

        html.H2('What question we are answering?'),

        html.Li('How many people in room we should have in order to have 50% probability of having AT LEAST two people with same birthday?'),
        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),

        html.H2('Why is it called paradox?'),

        html.Li([

        ]),

        html.Li([

        ]),
        html.Br(),

        html.Hr(),
        html.Hr(),

        dmc.Space(h=80),

        html.H2('What are assumptions of model/analysis?'),

        html.Li([
            'Year has 365 days'
        ]),

        html.Br(),

        html.Li([
            'There is no leap year (29th of February does not exist)'
        ]),

        html.Br(),

        html.Li([
            'There are no twins'
        ]),

        html.Br(),

        html.Li([
            'Probability of having a birth on any specific day is uniformly distributed i.e. there is equal chance to be born on each day (1/365) .'
        ]),

        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),
        html.H2('Why is important this paradox? What can we learn?'),

        html.Li([

        ]),

        html.Li([

        ]),

        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),
        html.H2('How we make decisions? Do we understand question before answering it?'),

        html.Li([

        ]),

        html.Li([

        ]),

        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),
        html.H2('What about intuition? Do we trust our intuition?'),

        html.Li([

        ]),

        html.Li([

        ]),

        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),
        html.H2('Conclusion:'),

        html.Li([
            'Be careful when you make decision based on intuition!'
        ]),

        html.Li([
            'Do not take yourself too serious when making decision based on intuition!'
        ]),
        
        html.Br(),
        html.Hr(),
        html.Hr(),

        html.Br(),

        dmc.Space(h=60)



    ])


