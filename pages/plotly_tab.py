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


def plotly_tab(df):
    return dmc.Container([

        dmc.Space(h=30),

        dmc.SimpleGrid([

            dmc.Paper([

                dmc.Title('Sample title', style={'textAlign': 'center'}),

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

        dmc.Space(h=60)

    ], fluid=True)
