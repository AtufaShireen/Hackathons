from dash import callback, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

file_path = r'C:\projects\dashboards_dash\data\suicides_preprocessed.csv'
df = pd.read_csv(file_path)

q = df[(df['new_state'] != 'TOTAL (ALL INDIA)')& (df['new_state'] != 'TOTAL (STATES)') & (df['new_state'] != 'TOTAL (UTs)') & (df['Age_group']!='0-100+')]
q = q.groupby(['new_state','Year','Gender'],as_index=False)['Total'].agg('sum')

# app = Dash(__name__)

layout = html.Div([
    html.H1(children='No. Of Suicides For 12 Years For Different Years'),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        q['Year'].min(),
        q['Year'].max(),
        step=None,
        value=q['Year'].min(),
        marks={str(Year): str(Year) for Year in q['Year'].unique()},
        id='Year-slider'
    ),
    dcc.Link('next', href='/page4')
])


@callback(
    Output('graph-with-slider', 'figure'),
    Input('Year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = q[q.Year == selected_year]

    fig = px.bar(filtered_df, x='new_state', y='Total',color='Gender', barmode="group")


    fig.update_layout(transition_duration=500)

    return fig

