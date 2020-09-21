import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

def init_dashboard(server):
    app = dash.Dash(
        __name__, 
        server=server,
        url_base_pathname="/dash/"
    )

    app.layout = html.Div(children = [
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
                        {'label':'Penalties Faced','value':'pens_att_gk'},
                        {'label':'Penalties Saved','value':'pens_saved'},
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
                        {'label':'Penalties Faced','value':'pens_att_gk'},
                        {'label':'Penalties Saved','value':'pens_saved'},
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
            html.H4(children = 'What is FPL?',style={'marginBottom':-10}),
            html.P(children = 'To keep it short, It’s an online game, well more than just a game, that puts you in the shoes of a fantasy manager in Premier League, where you pick real-life players that score points for you depending on their on-field performances.'),
            html.H5(children = 'Some of the stats used',style ={'marginBottom':-15}),
            dcc.Markdown('''
            I'm focusing on keepers mainly so here are some of the stats and their explanation:-
            * Save Percentage --> (Shots on Target Against - Goals Against)/Shots on Target Against
            * Clean Sheet Percentage --> Percentage of matches that result in the keeper not conceding any goals
            * Post Shot Expected Goals (PSxG) - Goals Allowed --> Positive numbers suggest better luck or an above average ability to stop shots. PSxG is expected goals based on how likely the goalkeeper is to save the shot. (xG totals include penalty kicks, but do not include penalty shootouts).
            * PPM or Points per minute --> Points earned last season by the player/Minutes player last season
            '''
            ),
            html.H5(children = 'More stuff coming up',style={'marginBottom':-10}),
            html.P(children = 'Analytics Panel for Forwards, Midfielders and Defenders.'),
            html.H4(children = 'Few links that can come in handy',style={'marginBottom':0}),
            html.A(' - More Info on PSxG',href='https://statsbomb.com/2018/11/a-new-way-to-measure-keepers-shot-stopping-post-shot-expected-goals/',target = '_blank'),
            html.Br(),
            html.A(' - Statisfy -  A collections of Basic Football Analytics',href='https://github.com/sidthakur08/statisfy'),
            html.Br(),
            html.A(' - Contact me on Twitter :)',href = 'https://twitter.com/sidtweetsnow',target='_blank'),
            html.Br(),
        ]),

        html.Div(className = 'link-name', children = [
            html.A('Link to the github repository',href = "https://github.com/sidthakur08/fpl_explore",target='_blank')
        ])
    ])

    init_callbacks(app)

    return app.server

def init_callbacks(app):
    @app.callback(
        Output('stats-graph','figure'),
        [
            Input('yaxis','value'),
            Input('xaxis','value'),
            Input('plot','value')
        ]
    )
    def update_graph(y,x,plot_type):
        keeper_data = pd.read_csv('./nbs/data/keeper_dash.csv')
        
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

    