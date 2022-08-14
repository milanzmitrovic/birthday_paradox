from dash import Dash, dcc, html


app = Dash(__name__)


def f1():
    return dcc.Markdown('''
    * Item 1
    * Item 2
    * Item 2a
    * Item 2b
''')


app.layout = html.Div([
    f1()
])


if __name__ == '__main__':
    app.run_server(debug=True)


