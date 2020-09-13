import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio


app = dash.Dash()

custom = dict(
    layout=go.Layout(title_font=dict(family="Rockwell", size=24, color="#28D0B4"))
)

keeper_data = pd.read_csv('keeper_dash.csv')

psxg_fig = px.bar(keeper_data,x='short_name',y='psxg_net_gk',text='psxg_net_gk')
psxg_fig.update_layout({
    'title':{
        'text':'PSxG - Goal Allowed per 90s',
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
        'title':'PSxG +/-',
        'showgrid':False,
    },
    'xaxis':{
        'title':'Keepers',
        'showgrid':False,
        'categoryorder':'total descending'
    },
    'font':{
        'family':'Rockwell',
        'color':'#28D0B4'
    },
})
psxg_fig.update_traces({
    'texttemplate':'%{text:.2s}',
    'textposition':'outside'
})

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

    dcc.Graph(
        id='psxg-net-graph',
        figure=psxg_fig,
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
