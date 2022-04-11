# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

file_path = r'C:\projects\dashboards_dash\data\suicides_preprocessed.csv'
df = pd.read_csv(file_path)

q = df[(df['new_state'] != 'TOTAL (ALL INDIA)')& (df['new_state'] != 'TOTAL (STATES)') & (df['new_state'] != 'TOTAL (UTs)') & (df['Age_group']!='0-100+')]

q = q.groupby(['Age_group','Gender'],as_index=False)['Total'].agg('sum')
del df
q = q.sort_values(by='Total',ascending=False)

fig = px.bar(q, x='Age_group', y='Total', barmode="group",color='Gender')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(children=[
    html.H1(children='No. Of Suicides For 12 Years By Age group'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Link('next', href='/page6')
])

