import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

APP_ID = 'keeper'
URL_BASE = '/dash/attacker/'

def init_attacker(server):
    app = dash.Dash(
        server=server,
        url_base_pathname=URL_BASE,
        suppress_callback_exceptions=True,
    )

    app.layout = html.Div(children = [
        html.H1(
            children = 'Fantasy Premier League Attack/Midfield Dashboard',
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
                        {'label':'Players','value':'player'},
                        {'label':'Games','value':'games'},
                        {'label':'Minutes','value':'minutes'},
                        {'label':'Total 90s','value':'minutes_90s'},
                        {'label':'Goals per90','value':'goals_per90'},
                        {'label':'Assists per90','value':'assists_per90'},
                        {'label':'Penalties Attempted','value':'pens_att'},
                        {'label':'Penalty Conversion %','value':'pens_conv'},
                        {'label':'Yellow Cards','value':'cards_yellow'},
                        {'label':'Red Cards','value':'cards_red'},
                        {'label':'Goals & Assists per90','value':'goals_assists_per90'},
                        {'label':'Goals + Assists - Penalties per90','value':'goals_assists_pen_per90'},
                        {'label':'Expected Goals per90','value':'xg_per90'},
                        {'label':'Expected Assists per90','value':'xa_per90'},
                        {'label':'xG & xA per90','value':'xg_xa_per90'},
                        {'label':'Non-Penalty Expected goals per90','value':'npxg_per90'},
                        {'label':'npxG + xA per90','value':'npxg_xa_per90'},
                        {'label':'xG_net','value':'xg_net'},
                        {'label':'Cost','value':'cost'},
                        {'label':'Points earned','value':'points'},
                        {'label':'Points per game','value':'ppg'},
                        {'label':'Points per cost','value':'ppc'}
                    ],
                    placeholder = 'Choose statistics for Y axis',
                    searchable = True,
                    value = 'points'
                ),
                dcc.Dropdown(
                    id = 'xaxis',
                    className = 'xdropdown',
                    options = [
                        {'label':'Players','value':'player'},
                        {'label':'Games','value':'games'},
                        {'label':'Minutes','value':'minutes'},
                        {'label':'Total 90s','value':'minutes_90s'},
                        {'label':'Goals per90','value':'goals_per90'},
                        {'label':'Assists per90','value':'assists_per90'},
                        {'label':'Penalties Attempted','value':'pens_att'},
                        {'label':'Penalty Conversion %','value':'pens_conv'},
                        {'label':'Yellow Cards','value':'cards_yellow'},
                        {'label':'Red Cards','value':'cards_red'},
                        {'label':'Goals & Assists per90','value':'goals_assists_per90'},
                        {'label':'Goals + Assists - Penalties per90','value':'goals_assists_pen_per90'},
                        {'label':'Expected Goals per90','value':'xg_per90'},
                        {'label':'Expected Assists per90','value':'xa_per90'},
                        {'label':'xG & xA per90','value':'xg_xa_per90'},
                        {'label':'Non-Penalty Expected goals per90','value':'npxg_per90'},
                        {'label':'npxG + xA per90','value':'npxg_xa_per90'},
                        {'label':'xG_net','value':'xg_net'},
                        {'label':'Cost','value':'cost'},
                        {'label':'Points earned','value':'points'},
                        {'label':'Points per game','value':'ppg'},
                        {'label':'Points per cost','value':'ppc'}
                    ],
                    placeholder = 'Choose statistics for X axis',
                    searchable = True,
                    value= 'player'
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
            html.H5(children = 'Some of the stats used',style ={'marginBottom':-2}),
            dcc.Markdown('''
            '''
            ),
            html.A(' - Statisfy -  A collections of Basic Football Analytics',href='https://github.com/sidthakur08/statisfy'),
            html.Br(),
            html.A(' - Contact me on Twitter :)',href = 'https://twitter.com/sidtweetsnow',target='_blank'),
            html.Br(),
        ]),

        html.Div(className = 'link-name', children = [
            html.A('Link to the github repository',href = "https://github.com/sidthakur08/fpl_explore",target='_blank')
        ]),
        html.Br(),
        html.Br(),
        html.Br(),
    ])

    init_attacker_callbacks(app)

    return app.server

def init_attacker_callbacks(app):
    @app.callback(
        Output('stats-graph','figure'),
        [
            Input('yaxis','value'),
            Input('xaxis','value'),
            Input('plot','value')
        ]
    )
    def update_graph(y,x,plot_type):
        keeper_data = pd.read_csv('./data/attacker_dash.csv')
        
        if plot_type=='bar':
            fig = px.bar(keeper_data,x=x,y=y,hover_name='player',hover_data=['cost','points','squad','position','minutes'])
        elif plot_type=='scatter':
            fig = px.scatter(keeper_data,x=x,y=y,hover_name='player',hover_data=['cost','points','squad','position','minutes'])

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



'''html.H5(children = 'More stuff coming up',style={'marginBottom':-10}),
        html.P(children = 'Analytics Panel for Forwards, Midfielders and Defenders.'),
        html.H4(children = 'Few links that can come in handy',style={'marginBottom':0}),
        html.A(' - More Info on PSxG',href='https://statsbomb.com/2018/11/a-new-way-to-measure-keepers-shot-stopping-post-shot-expected-goals/',target = '_blank'),
        html.Br(),'''