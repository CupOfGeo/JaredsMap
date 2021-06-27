import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(id='address_input',type="search", placeholder="Search", size='500', style={'fontSize': '500%'})),
        dbc.Col(
            dbc.Button("Search",id='submit', color="primary", className="ml-2", n_clicks=0, size='lg', style={'height':'123px'}
            ),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

toast = html.Div(
    [
        dbc.Button(
            "Open toast",
            id="simple-toast-toggle",
            color="primary",
            className="mb-3",
            n_clicks=0,
        ),
        dbc.Toast(
            [html.P("This is the content of the toast", className="mb-0")],
            id="simple-toast",
            header="This is the header",
            icon="primary",
            dismissable=True,
            is_open=True,
        ),
    ]
)

single = dbc.Col(dbc.Row([html.Div("Grant Park",id='address_0'), dbc.Button('x')]))
# #class="toast-body"
# single = dbc.Toast(
#             [],
#             #id="simple-toast",
#             header="This is the header",
#             # icon="primary",
#             dismissable=True,
#             is_open=True,
#             style={}
#         )
# many_toasts = [single for x in range(5)]
# *many_toasts in a list

#navbar = \
app.layout = html.Div([dbc.Navbar(
    [
        dbc.Collapse(
            search_bar, id="navbar-collapse", navbar=True, is_open=True
        ),
    ],
    color="dark",
    dark=True,
    expand='lg',
    style={'height': '200px'}

),
    single
])


# @app.callback(
#     Output("simple-toast", "is_open"),
#     [Input("simple-toast-toggle", "n_clicks")],
# )
# def open_toast(n):
#     return True

@app.callback(Output('address_input','value'),
              Input('submit', 'n_clicks'),
              State('address_input','value'))
def add_address(click,value):
    # do something with the value
    value = ''
    return value



app.run_server(debug=True, use_reloader=True, host='0.0.0.0')  # Turn off reloader if inside Jupyter
