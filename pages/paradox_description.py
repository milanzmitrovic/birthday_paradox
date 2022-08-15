
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback


def paradox_description():
    return dmc.Container([

        dmc.Space(h=40),

        # html.H1('Main question that should be answered'),

        html.Br(),

        html.H2('What question we are answering?'),

        html.Li('How many people in room we should have in order to have 50% probability of having AT LEAST two people with same birthday?'),
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

        # ---- #
        html.H2('Why is it called paradox?'),

        html.Li([
            'There are 365 possible days when people can be born on'
        ]),

        html.Br(),

        html.Li([
            'We are interested in number of people that gives 50% probability of having two people with same birthday'
        ]),

        html.Br(),

        html.Li([
            'How much people we will need to have in group so that there is 50% probability...?'
        ]),

        html.Br(),

        html.Li(
            [
                'Intuitively, 50% of 365 is around 182'
            ],
            style={'margin-left': 30}
        ),

        html.Br(),

        html.Li(
            [
                'Is our intuition good?'
            ],
            style={'margin-left': 30}
        ),

        html.Br(),

        html.Li([
            'People usually understand this question following way:'
        ]),

        html.Br(),

        html.Li(
            [
                'How many people should be in room, so that there is 50% chance of sb else having same birthday as me.'
            ],
            style={'margin-left': 30}
        ),

        html.Br(),

        html.Hr(),
        html.Hr(),

        dmc.Space(h=80),

        # ----- #


        html.H2('What is wrong with our intuition?'),

        html.Li([
            'Our brain is very good at thinking linearly.'
        ]),

        html.Br(),

        html.Li([
            'We dismiss fact that we are NOT interested in two specific persons.'
        ]),

        html.Br(),

        html.Li([
            'We are interested in ANY two persons having same birthday.'
        ]),

        html.Br(),

        html.Li([
            'Nonlinear effects, each person is checking his birthday with everyone else!!!'
        ]),

        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),
        html.H2('How we make decisions? Do we understand question before answering it?'),

        html.Li([
            'How many times you participated in discussions when two people talking about two different things (they are not on the same page)?'

        ]),

        html.Br(),

        html.Li([
            'Do you always make sure you understand question before answering it?'
        ]),

        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),
        html.H2('What about intuition? Do we trust our intuition?'),

        html.Li([
            'What is story behind intuition?'
        ]),

        html.Br(),

        html.Li([
            'What is basis of gut feeling'
        ]),

        html.Br(),

        html.Hr(),
        html.Hr(),
        dmc.Space(h=80),
        html.H2('Conclusion:'),

        html.Li([
            'Be careful when you make decision based on intuition!'
        ]),

        html.Br(),

        html.Li([
            'Do not take yourself too serious when making decision based on intuition!'
        ]),

        html.Br(),

        html.Li([
            'How many times you participated in discussions when two people talking about two different things?'
        ]),

        html.Br(),
        html.Hr(),
        html.Hr(),

        html.Br(),

        dmc.Space(h=60)



    ])


