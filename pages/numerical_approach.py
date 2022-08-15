
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback


def numerical_approach():

    return dmc.Container([

        dmc.Space(h=40),

        # ------------------------------------------------------ #
        html.H2('Following terms should be defined:'),

        html.Li('Sample (i.e. room with people)'),
        html.Br(),

        html.Li('Sample size (how many people in room)'),
        html.Br(),

        html.Li('Number of sample'),
        html.Br(),

        html.Li('Experiment'),
        dmc.Space(h=50),


        # ------------------------------------------------------ #
        html.H2('Steps for performing numerical calculations:'),

        html.Li('Choose sample size you like (e.g. 10 people should be in room)'),
        html.Br(),

        html.Li(
            'What is probability that there are at least two people sharing same birthday, if there are 10 persons in room?',
            style={'margin-left': 30}
        ),
        html.Br(),

        html.Li('Decide how many times you will run experiment'),
        html.Br(),

        html.Li(
            'The more times you run experiment, more close to real world probability you will be!',
            style={'margin-left': 30}
        ),
        html.Br(),

        html.Li('Run experiment (specific number of times)'),
        html.Br(),

        html.Li('Check how many times happened case with two or more people sharing same birthday'),
        html.Br(),

        html.Li('Calculate probability (Number of samples with at least 2 people sharing same birthday / Number of experiments generated (third step))'),
        dmc.Space(h=50),

        html.H2('Example'),

        html.Li([
            html.A("Link to example", href='https://gist.github.com/milanzmitrovic/134bfc31a3a9540bf2b4f14ceeac56f9', target="_blank")
        ]),

        dmc.Space(h=70),

    ])




# Analytic VS Numeric approach
# More intuitive? -->
# More general? -->
# Older? -->
# More modern? -->
# Computationally efficient? -->


# Analytical approach:
# count(number of cases we like) / count(number of all possible cases) * 100


# We will use small trick :)

# Instead of calculating probability of having of AT LEAST two matching birthdays,
# lets calculate probability of NOT having at least two birthdays.

# [probability of having at least two birthdays] + [probability of NOT having at least two birthdays] = 1
# So, [probability of having at least two birthdays] = 1 - [probability of NOT having at least two birthdays]


# 365/365 * 364/365
#
# n = 365
# # Probability of not having two people sharing same birthday
# prob = 1
# for i in range(90):
#     prob = prob * (n - i) / 365
#
#     print(i, 'Probability of not having common birthdays', prob)
#     print(i, 'Probability of having common birthdays', 1 - prob)
#     print('---------')
#
#




