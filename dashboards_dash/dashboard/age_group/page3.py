# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

file_path = r'C:\projects\dashboards_dash\data\suicides_preprocessed.csv'
df = pd.read_csv(file_path)

q = df[(df['new_state'] != 'TOTAL (ALL INDIA)')& (df['new_state'] != 'TOTAL (STATES)') & (df['new_state'] != 'TOTAL (UTs)') & (df['Age_group']!='0-100+')]

q = q.groupby(['Type_code','Age_group'],as_index=False)['Total'].agg('sum')
q = q.sort_values(by='Total',ascending=False)

fig = px.bar(x=q['Age_group'], y=q['Total'], barmode="group",color=q['Type_code'])

q = df[(df['new_state'] == 'TOTAL (ALL INDIA)')& (df['new_state'] != 'TOTAL (STATES)') & (df['new_state'] != 'TOTAL (UTs)') & (df['Age_group'] =='0-100+')]

q = q.groupby(['Age_group','Type_code'],as_index=False)['Total'].agg('sum')
q = q.sort_values(by='Total',ascending=False)
del df
fig2 = px.bar(x=q['Age_group'], y=q['Total'], barmode="group",color=q['Type_code'])

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(style={'backgroundColor': colors['background'],'color': colors['text'], 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px','bottom':'0px'},
children=[
    html.H1(children='No. Of Suicides For 12 Years By Age group'),
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
    dcc.Link('next', href='/page7'),
])

