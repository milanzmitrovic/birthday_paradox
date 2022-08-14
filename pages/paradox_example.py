import numpy as np
import pandas as pd
from pydantic import validate_arguments
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_mantine_components as dmc


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


@validate_arguments()
def data_generation(
        number_of_people_in_room: int,
        sample_size: int
) -> pd.DataFrame:
    np_array = np.random.randint(low=1,
                                 high=366,
                                 size=[number_of_people_in_room, sample_size]
                                 )
    return pd.DataFrame(
        data=np_array
    )


@validate_arguments(config={'arbitrary_types_allowed': True})
def does_match_happen(s: pd.Series) -> int:
    if s.value_counts().sum() > s.value_counts().size:
        return 1
    else:
        return 0


@validate_arguments(config={'arbitrary_types_allowed': True})
def create_binary_representation_of_sample_data(df: pd.DataFrame) -> pd.Series:
    return df.apply(does_match_happen, axis=0)


@validate_arguments(config={'arbitrary_types_allowed': True})
def create_probability(s: pd.Series) -> float:
    return s.sum() / s.size


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
    for i in range(60):
        df = data_generation(
            number_of_people_in_room=i,
            sample_size=sample_size
        )

        probability = (
            df.pipe(func=create_binary_representation_of_sample_data)
                .pipe(func=create_probability)
        )

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

    return fig


@callback(
    Output("drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
