import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly

app = dash.Dash()


if __name__ == "__main__":
    app.run_server(debug=True)
