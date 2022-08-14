
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback


def paradox_description():
    return dmc.Container([

        html.H1('What question we are answering?'),

        html.H1('How many people in room we should have in order to have 50% probability of having AT LEAST two people with same birthday?'),

        html.H1('What are assumptions of model/analysis?'),

        dcc.Markdown(['''
        
            * Year has 365 days
            * There is no leap year (29th of February does not exist)
            * There are no twins
            * Probability of having a birth on any specific day is uniformly distributed i.e. there is equal chance to be born on each day (1/365) .
        
        '''])

    ], fluid=True)


