import numpy as np
import pandas as pd
from pydantic import validate_arguments
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_mantine_components as dmc

from utils.paradox_functions.paradox_functions import data_generation, create_binary_representation_of_sample_data, \
    create_probability


def graph_component():
    return dmc.Skeleton(
        dcc.Graph(
            id='scatter_plot'
        ),
        visible=False
    )


def run_btn():
    return dmc.Button(
        'Run experiment',
        id='btn-start'
    )


def sample_size_filter():
    return dmc.NumberInput(
        id='sample_size_filter',
        value=15,
        min=5,
        max=100
    )


def drawer_component():
    return html.Div(
        [
            dmc.Button("Open Drawer", id="drawer-demo-button"),
            dmc.Drawer(
                [
                    html.Br(),
                    sample_size_filter(),
                    html.Br(),
                    html.Br(),
                    run_btn()
                ],
                title="Filter Section",
                id="drawer",
                padding="md",
            ),

        ]
    )


def create_layout():
    return dmc.Container(
        fluid=True,
        style={'padding': '0px'},
        children=[

            dmc.Space(h=20),

            drawer_component(),

            dmc.Space(h=60),

            graph_component(),

            dmc.Space(h=40)

        ])


@callback(
    Output(component_id='scatter_plot', component_property='figure'),
    Input(component_id='btn-start', component_property='n_clicks'),
    State(component_id='sample_size_filter', component_property='value'),
)
def main_app_logic(
        number_of_clicks,
        sample_size

):
    number_of_people_on_birthday = []
    probability_list = []
    number_of_birthday_matches = []
    number_of_people_in_group = []
    for i in range(60):
        df = data_generation(
            number_of_people_in_room=i,
            sample_size=sample_size
        )

        probability = (
            df.pipe(func=create_binary_representation_of_sample_data)
                .pipe(func=create_probability)
        )

        number_of_birthday_matches.append(create_binary_representation_of_sample_data(df).sum())
        number_of_people_in_group.append(create_binary_representation_of_sample_data(df).__len__())

        number_of_people_on_birthday.append(i)
        probability_list.append(probability)

    df_final = pd.DataFrame(
        {
            'Number of people in room': number_of_people_on_birthday,
            'Probability': probability_list
        }
    )

    fig = px.scatter(
        x=df_final.filter(items=['Number of people in room'], axis=1).values[:, 0],
        y=df_final.filter(items=['Probability'], axis=1).values[:, 0],
        template='simple_white',
        title='Birthday Paradox'
    )

    fig.update_layout(xaxis_title="Number of People in room",
                      yaxis_title="Probability of having at least two persons born on same day",
                      title_x=0.5
                      )

    fig.update_xaxes(showspikes=True)

    return fig


@callback(
    Output("drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
