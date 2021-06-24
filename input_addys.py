import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(
    [
        #dbc.Input(id='addy'),
        dbc.Button(
            "Add Stop",
            id="simple-toast-toggle",
            color="primary",
            className="mb-3",
            n_clicks=0,
        ),
        html.Div(id='div_list'),

    ]
)


@app.callback(
    # Output("simple-toast", "is_open"),
    # Output("simple-toast", "header"),
    Output('div_list', 'children'),
    [Input("simple-toast-toggle", "n_clicks")],
    #State('addy', 'value'),
    State('div_list', 'children')
)
def open_toast(n, kids):
    print(kids)
    print('-'*52)
    idxs = []
    if kids:
        for kid in kids:
            props_dic = kid['props']
            idxs.append(props_dic['id'])

        idx = [int(x) for x in idxs]
        next_idx = 1
        new_kid = {'props': {'id': next_idx}, 'type': 'Input', 'namespace': 'dash_bootstrap_components'}
        kids.append(new_kid)

    else:
        # first Kid
        kids = []

        new_kid = {'props': {'id': 0}, 'type': 'Input', 'namespace': 'dash_bootstrap_components'}
        kids.append(new_kid)
    return kids
'''
[{'props': {'id': '2'}, 'type': 'Input', 'namespace': 'dash_bootstrap_components'}, 
{'props': {'id': '3'}, 'type': 'Input', 'namespace': 'dash_bootstrap_components'}]'''



app.run_server(debug=True, use_reloader=True, host='0.0.0.0')  # Turn off reloader if inside Jupyter