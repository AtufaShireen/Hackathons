# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

file_path = r'C:\projects\dashboards_dash\data\suicides_preprocessed.csv'
df = pd.read_csv(file_path)

q = df[(df['new_state'] == 'TOTAL (ALL INDIA)')& (df['Age_group']=='0-100+') &(df['Type_code']=='Social_Status')]
q = q.groupby(['Year','Type'],as_index=False)['Total'].sum()
fig = px.line( q,x='Year',y='Total',color='Type',markers=True,title='Social status and suicides over year')

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
q = df[(df['new_state'] == 'TOTAL (ALL INDIA)')& (df['Age_group']=='0-100+') &(df['Type_code']=='Education_Status')]
q = q.groupby(['Year','Type'],as_index=False)['Total'].sum()
fig2 = px.line( q,x='Year',y='Total',color='Type',markers=True,title='Education status and suicides over year')

fig2.update_layout(margin = dict(t=50, l=25, r=25, b=25))
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(style={'backgroundColor': colors['background'],'color': colors['text'], 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px','bottom':'0px'},
children=[
    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={'display':'inline-block'}
    ),
        dcc.Graph(
        id='example-graph2',
        figure=fig2,
        style={'display':'inline-block'}
    ),
    dcc.Link('next', href='/page10'),
]

)
