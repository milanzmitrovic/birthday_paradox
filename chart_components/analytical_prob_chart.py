

import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px


def generate_analytical_chart():

    n = 365
    prob_of_not = 1

    number_of_people_in_room = []
    probability_of_having_match = []

    for i in range(90):

        number_of_people_in_room.append(i)
        prob_of_not = prob_of_not * (n - i) / 365

        probability_of_having_match.append(1-prob_of_not)

    fig = px.scatter(
        x=number_of_people_in_room,
        y=probability_of_having_match,
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=10, l=10, r=10, b=10),
        yaxis_title='Probability of having at least two people sharing birthday',
        xaxis_title='Number of people in room'
    )

    return dcc.Graph(figure=fig)



