import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from geopy.geocoders import Nominatim
import time
from pprint import pprint
# instantiate a new Nominatim client
geo = Nominatim(user_agent="tutorial")
location = geo.geocode("56 East Rockaway rd. Hewlett, New York").raw
# print raw data
# pprint(location)

mapbox_access_token = "pk.eyJ1IjoiY3Vwb2ZnZW8iLCJhIjoiY2txYjlxbGh1MDAxODJybDRqY3d5eHk2OCJ9.G1BxZ3CVKgW_p98xFrg1aQ"

fig = go.Figure(go.Scattermapbox(
        lat=[location['lat']],
        lon=[location['lon']],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=["home"],
    ))

fig.update_layout(
    height = 1000,
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

import plotly.graph_objects as go # or plotly.express as px



import dash_bootstrap_components as dbc
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app = dash.Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.LUX])
app.layout = dbc.Container([dbc.Textarea(id='addys', value='',style={'width': '100%'}),
                       dbc.Button('Submit', id='submit'),
                       dcc.Graph(figure=fig,id='map'),])

@app.callback(Output('map','figure'),
              Input('submit','n_clicks'),
              State('addys','value'))
def loc(click,value):
    pprint(value)
    values = value.split('\n')
    lats = []
    lons = []

    if value == '':
        raise PreventUpdate
    for value in values:
        location = geo.geocode(value).raw
        lats.append(location['lat'])
        lons.append(location['lon'])

    mean_lat = sum([float(x) for x in lats])/len(lats)
    mean_lon = sum([float(x) for x in lons])/len(lons)
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
            zoom=13
        ),

    )
    return fig

app.run_server(debug=True)  # Turn off reloader if inside Jupyter

server = app.server
app.title='JaredsMapApp'