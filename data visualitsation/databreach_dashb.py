from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


df = pd.read_csv('/home/craver/academic/python/pythonProject/data visualitsation/Top20.csv')
# Initialize the app - incorporate css

app = Dash(__name__)
# -------------------bar chart------------------------------------
fig = px.histogram(df, x = 'Records', y = 'Company',template='plotly_dark')

# ---------------------------pie chart-------------------------
pie_chart = px.pie(df, values='Records', names='Organization type', title='Effect on different secotrs',template='plotly_dark')

pie_chart.update_traces(
    textfont=dict(color='white'),  # Set text color to white
    pull=[0.1, 0, 0, 0, 0]  # Optional: Add some pull effect to make the first slice pop out
)


# --------------------------Line chart--------------------------
line_chart = px.line(df, x='Year', y='Records' , title='Data breaches in each year', markers=True,
                     template='plotly_dark')


# Define the layout
app.layout = html.Div(children=[
    html.Div(children='Data Breach Records', style={'text-align': 'center', 'font-size': '24px', 'padding': '20px'}),
    html.Hr(),
    
    # First div for the bar graph
    html.Div([
        dcc.Graph(figure=fig, id='bar_graph')
    ], className='graph_container'),
    
    # Second div for the pie chart
    html.Div([
        dcc.Graph(figure=pie_chart, id='pie_graph'),
        dcc.Graph(figure=line_chart, id='line_chart')
    ],className='graph-container'),
])


if __name__ == '__main__':
    app.run(debug=True)