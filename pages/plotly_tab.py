import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import pandas as pd

from chart_components.bar_chart import bar_chart
from chart_components.bar_chart_grouped import bar_chart_grouped
from chart_components.bar_chart_stacked import bar_chart_stacked
from chart_components.donut_chart import donut_chart
from chart_components.icicle_chart import icicle_chart
from chart_components.line_chart import line_chart
from chart_components.pie_chart import pie_chart
from chart_components.scatter_plot import scatter_plot
from chart_components.sunburst_chart import sunburst_chart
from chart_components.treemap_chart import treemap_chart


# Plotly

# Open source library
# High level API
# Different languages supported - Python, r, Julia, .Net
# Very intuitive and easy to use
#   Even more intuitive than GUI tools
#   But with big advantage - It is written in code (Version controle, ...)

# EXAMPLES


def plotly_tab(df):
    return dmc.Container([

        dmc.Space(h=40),

        dmc.Container([

            html.H2('Open source library'),

            html.Li('Free to use even for commercial purpose!'),

            dmc.Space(h=30),

            html.H2('High level API'),

            html.Li('Plotly Expres - Very intuitive'),

            dmc.Space(h=30),

            html.H2('Many languages supported'),

            html.Li('Python'),
            html.Br(),
            html.Li('R'),
            html.Br(),
            html.Li('Julia'),
            html.Br(),
            html.Li('.Net'),

            dmc.Space(h=30),

            html.H2('Very intuitive and easy to use'),

            html.Li('Even more intuitive than GUI tools'),

            html.Li('But with big advantage - It is written in code (Version controle, ...)'),

            dmc.Space(h=70),

            html.H1('Plotly Examples', style={'textAlign': 'center'})

        ]),

        dmc.Space(h=30),

        dmc.SimpleGrid([

            dmc.Paper([

                dmc.Title('Bar Chart', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=bar_chart(
                        df=df,
                        x_axis='Segment',
                        y_axis='Profit',
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Bar Chart Grouped', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=bar_chart_grouped(
                        df=df,
                        x_axis='Segment',
                        y_axis='Profit',
                        color='Ship Mode'
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Bar Chart Stacked', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=bar_chart_stacked(
                        df=df,
                        x_axis='Segment',
                        y_axis='Profit',
                        color='Ship Mode'
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Donut Chart', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=donut_chart(
                        df=df,
                        labels='Ship Mode',
                        values='Profit',
                        hole_size=0.6,
                        title='Test Chart Pie'
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Icicle Chart', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=icicle_chart(
                        df=df,
                        dimensions=['Segment', 'Category', 'Sub-Category'],
                        metric='Sales'
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Pie Chart', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=pie_chart(
                        df=df,
                        labels='Ship Mode',
                        values='Profit',
                        title='Test Pie Chart 1'
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Sunburst Chart', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=sunburst_chart(
                        df=df,
                        dimensions=['Segment', 'Category', 'Sub-Category'],
                        metric='Sales'
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Treemap Chart', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=treemap_chart(
                        df=df,
                        dimensions=['Segment', 'Category', 'Sub-Category'],
                        metric='Sales'
                    )
                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            dmc.Paper([

                dmc.Title('Scatter Plot', style={'textAlign': 'center'}),

                dcc.Graph(
                    figure=scatter_plot(
                        df=df,
                        x_axis="Quantity",
                        y_axis="Sales",
                        color="Profit"
                    )

                )

            ],
                withBorder=True,
                radius='lg',
                shadow='xl'),

            line_chart(
                df=df,
                x_axis='Order Date',
                y_axis='Sales'
            )

        ],
            breakpoints=[
                {"maxWidth": 1300, "cols": 3, "spacing": "md"},
                {"maxWidth": 980, "cols": 2, "spacing": "sm"},
                {"maxWidth": 750, "cols": 1, "spacing": "sm"},
            ],
            cols=3
        ),

        dmc.Space(h=60),

        html.Li([
            html.A("Link to GitHub gists", href='https://gist.github.com/milanzmitrovic/134bfc31a3a9540bf2b4f14ceeac56f9',
                   target="_blank")
        ], style={'textAlign': 'center'}),

        dmc.Space(h=70),

    ], fluid=True)



