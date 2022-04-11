# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# app = Dash(__name__)

file_path = r'C:\projects\dashboards_dash\data\suicides_preprocessed.csv'
df = pd.read_csv(file_path)

q = df[(df['new_state'] == 'MH') & (df['Age_group'] =='0-100+')]
q = q.groupby(['Year','Gender'],as_index=False)['Total'].sum()

fig_line = px.line(x=q['Year'], y=q['Total'], color=q['Gender'],title='Trend in Suicides ')
fig_line.update_layout(margin = dict(t=50, l=25, r=25, b=25))
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig_line.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

q = df[(df['new_state'] == 'MH') & (df['Age_group'] !='0-100+')]
fig_pie = px.pie(q, values='Total', names='Age_group',title='Age distribution of Suicides ')
fig_pie.update_layout(margin = dict(t=50, l=25, r=25, b=25))
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig_pie.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

q = df[(df['new_state'] == 'MH') & (df['Age_group'] !='0-100+') &(df['Type_code']=='Causes')].sort_values(by='Total')
fig_bar = px.bar(q, x='Total', y='Type',barmode='group',title='causes of Suicides ')
fig_bar.update_layout(margin = dict(t=50, l=25, r=25, b=25))
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig_bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

q = df[(df['new_state'] == 'MH') & (df['Age_group'] !='0-100+') &(df['Type_code']=='Means_adopted')]
fig_tree = px.treemap(q[q['Type_code']=='Means_adopted'], values='Total', path=['Type'],title='Method Used for commiting suicide')
fig_tree.update_layout(margin = dict(t=50, l=25, r=25, b=25))
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig_tree.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(style={'backgroundColor': colors['background'],'color': colors['text'], 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px'},
children=[
    html.H1(children='Maharashtra profile for Suicides '),
    dcc.Graph(
        id='line-graph',
        figure=fig_line,
        style={'display':'inline-block'}
    ),
    
        dcc.Graph(
        id='bar-graph',
        figure=fig_bar,
        style={'display':'inline-block'}
    ),
    html.H1(children='       '),
        dcc.Graph(
        id='pie-graph',
        figure=fig_pie,
        style={'display':'inline-block'}
    ),
        dcc.Graph(
        id='tree-graph',
        figure=fig_tree,
        style={'display':'inline-block'}
    ),
    dcc.Link('next', href='/'),
])

