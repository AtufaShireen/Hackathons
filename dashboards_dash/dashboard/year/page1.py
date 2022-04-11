# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import  html, dcc,callback
import plotly.express as px
import pandas as pd

# app = Dash(__name__)

file_path = r'C:\projects\dashboards_dash\data\suicides_preprocessed.csv'
df = pd.read_csv(file_path)

q = df[(df['new_state'] != 'TOTAL (ALL INDIA)')& (df['new_state'] != 'TOTAL (STATES)') & (df['new_state'] != 'TOTAL (UTs)') & (df['Age_group']!='0-100+')]
del df
q = q.groupby('new_state',as_index=False)['Total'].agg('sum')
q = q.sort_values(by='Total',ascending=False)

fig = px.bar(q, x=q['new_state'], y=q['Total'], barmode="group")

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(style={'backgroundColor': colors['background'],'color': colors['text'], 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px','bottom':'0px'},
children=[
    html.H1(children='No. Of Suicides For 12 Years, Statewise'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Link('next', href='/page3')
])

