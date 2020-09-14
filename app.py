import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

app = dash.Dash()

custom = dict(
    layout=go.Layout(title_font=dict(family="Rockwell", size=24, color="#28D0B4"))
)

keeper_data = pd.read_csv('keeper_dash.csv')

app.layout = html.Div(style={
    'marginLeft': 0, 'marginRight': 0, 'marginTop': 0, 'marginBottom': 0,
    'backgroundColor':'#333', 'padding': '0px 0px 0px 0px'}, children = [
    html.H1(
        children = 'Fantasy Premier League Exploration Dashboard',
        style = {
            'textAlign':'center',
            'color':'#28D0B4',
        }
    ),
    html.Div(
        children = 'This interactive web app can be a toolkit for you to select and optimise your player selection based on their previous year\'s performances',
        style = {
            'color':'#28D0B4',
        }
    ),

    html.Div(
        id = 'stats-menu',
        className = 'dropdowns',
        children = [
            dcc.Dropdown(
                id = 'yaxis',
                className = 'ydropdown',
                options = [
                    {'label':'Games Played','value':'games_gk'},
                    {'label':'Minutes Played','value':'minutes_gk'},
                    {'label':'Save %','value':'save_pct'},
                    {'label':'Clean Sheet %','value':'clean_sheets_pct'},
                    {'label':'Penalties Allowed','value':'pens_allowed'},
                    {'label':'PSxG - Goals Allowed','value':'psxg_net_gk'},
                    {'label':'Cost','value':'cost'},
                    {'label':'Points','value':'points'},
                    {'label':'Points per minute','value':'ppm'},
                    {'label':'Players','value':'player_name'},
                ],
                placeholder = 'Choose statistics for Y axis',
                searchable = True,
                value = 'points'
            ),
            dcc.Dropdown(
                id = 'xaxis',
                className = 'xdropdown',
                options = [
                    {'label':'Games Played','value':'games_gk'},
                    {'label':'Minutes Played','value':'minutes_gk'},
                    {'label':'Save %','value':'save_pct'},
                    {'label':'Clean Sheet %','value':'clean_sheets_pct'},
                    {'label':'Penalties Allowed','value':'pens_allowed'},
                    {'label':'PSxG - Goals Allowed','value':'psxg_net_gk'},
                    {'label':'Cost','value':'cost'},
                    {'label':'Points','value':'points'},
                    {'label':'Points per minute','value':'ppm'},
                    {'label':'Players','value':'player_name'},
                ],
                placeholder = 'Choose statistics for X axis',
                searchable = True,
                value= 'player_name'
            ),
            dcc.RadioItems(
                id='plot',
                className = 'plot-select',
                options=[{'label': 'Bar Plot', 'value': 'bar'},
                         {'label': 'Scatter Plot', 'value': 'scatter'},
                ],
                value='scatter'
            ),
        ]
    ),

    dcc.Graph(
        id='stats-graph',
        className = 'graph',
        style = {
            'marginTop':40,
        }
    ),

    html.Div(className = 'info-panel',children=[
        html.H4(children = 'What is FPL?'),
        html.P(children = 'Helo?')
    ]),

    html.Div(className = 'link-name', children = [
        html.A('Link to the github repository',href = "https://github.com/sidthakur08/fpl_explore",target='_blank')
    ])
])

@app.callback(
    Output('stats-graph','figure'),
    [
        Input('yaxis','value'),
        Input('xaxis','value'),
        Input('plot','value')
    ]
)
def update_graph(y,x,plot_type):
    if plot_type=='bar':
        fig = px.bar(keeper_data,x=x,y=y,hover_name='player',hover_data=['cost','points','minutes_gk'])
    elif plot_type=='scatter':
        fig = px.scatter(keeper_data,x=x,y=y,hover_name='player',hover_data=['cost','points','minutes_gk'])

    fig.update_layout({
        'title':{
            'text':f'{y.capitalize()} vs {x.capitalize()}',
            'font':{
                'family':'Rockwell',
                'size':24,
                'color':'#28D0B4'
            },
            'x':0.5
        },
        'plot_bgcolor':'#333',
        'paper_bgcolor':'#333',
        'yaxis':{
            'title':f'{y.capitalize()}',
            'showgrid':False,
        },
        'xaxis':{
            'title':f'{x.capitalize()}',
            'showgrid':False,
            'categoryorder':'total descending'
        },
        'font':{
            'family':'Rockwell',
            'color':'#28D0B4'
        },
    })
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
