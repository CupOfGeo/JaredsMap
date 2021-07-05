import plotly.graph_objects as go  # or plotly.express as px
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from geopy.geocoders import Nominatim

from app import server, app
from google_directions_api import one_shot_url

# instantiate a new Nominatim client
geo = Nominatim(user_agent="tutorial")
location = geo.geocode("Hewlett, New York").raw
# print raw data
# pprint(location)

mapbox_access_token = "pk.eyJ1IjoiY3Vwb2ZnZW8iLCJhIjoiY2txYjlxbGh1MDAxODJybDRqY3d5eHk2OCJ9.G1BxZ3CVKgW_p98xFrg1aQ"

fig = go.Figure(go.Scattermapbox(
    lat=[],  # location['lat']
    lon=[],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=9
    ),
    text=["home"],
))

fig.update_layout(
    height=1000,
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.64,
            lon=-73.69
        ),
        pitch=0,
        zoom=13
    ),

)

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search", size='500', style={'fontSize': '500%'})),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ml-2", n_clicks=0, size='lg', style={'height': '123px'}
            ),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

app.layout = html.Div([
    # dbc.Navbar(
    #     [
    #         dbc.Collapse(
    #             search_bar, id="navbar-collapse", navbar=True, is_open=True
    #         ),
    #     ],
    #     color="dark",
    #     dark=True,
    #     expand='lg',
    #     style={'height': '200px'}
    #
    # ),
    dbc.Container([

        dbc.Textarea(id='addys', value='', style={'width': '100%'}),
        dbc.Button('Submit', id='submit'),
        html.P(id='route_out'),
        dcc.Graph(figure=fig, id='map'), ])
])


@app.callback(Output('map', 'figure'),
              Output('route_out', 'children'),
              Input('submit', 'n_clicks'),
              State('addys', 'value'))
def loc(click, value):
    base_url = 'https://www.google.com/maps/dir/'
    values = value.split('\n')

    lats = []
    lons = []

    cord_to_add = {}
    if value == '':
        raise PreventUpdate
    # print(values)
    for value in values:
        if value is not None:
            check = geo.geocode(value)
            if check is not None:
                location = check.raw
                lats.append(location['lat'])
                lons.append(location['lon'])
        else:
            # wrong address
            return '', f'{value} Address not found'
            print(value, 'address not found')

        cord_to_add[(float(location['lat']), float(location['lon']))] = value

    # get an optimal route from nearest neighbour and then print the order of the route
    addy_list = one_shot_url(values)
    base_url = 'https://www.google.com/maps/dir/'
    url = ''
    for addy in addy_list:
        url += "+".join(addy.split(' ')) + '/'
    url = base_url + url
    out = html.A('click for google maps gps', href=url,)

    mean_lat = sum([float(x) for x in lats]) / len(lats)
    mean_lon = sum([float(x) for x in lons]) / len(lons)
    fig = go.Figure(go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=values,
    ))

    fig.update_layout(
        height=1000,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=mean_lat,
                lon=mean_lon
            ),
            pitch=0,
            zoom=10
        ),

    )
    return fig, out  # (base_url + url)


if __name__ == "__main__":
    app.run_server(debug=True)  # Turn off reloader if inside Jupyter
