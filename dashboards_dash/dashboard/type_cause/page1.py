# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import base64
app = Dash(__name__)

# file_path = r'C:\projects\dashboards_dash\data\suicides_preprocessed.csv'
# df = pd.read_csv(file_path)

# q = df[ (df['Age_group']!='0-100+') &(df['Type_code']=='Professional_Profile') &(df['Total']>0)]
# crosstab = pd.crosstab(q["Type"], q["Age_group"])
# q= q.groupby(['Type','Age_group'])

# fig = px.bar(q, x=q["Type"], y= q["Age_group"], color = q['Age_group'],barmode="group")
# fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )
image_filename = r'C:\projects\dashboards_dash\data\age_cause.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('utf-8')  
image_filename_1 = r'C:\projects\dashboards_dash\data\age_cause_1.png'
encoded_image_1 = base64.b64encode(open(image_filename_1, 'rb').read()).decode('utf-8')  

image_filename_2 = r'C:\projects\dashboards_dash\data\gender_state.png'
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read()).decode('utf-8')  
image_filename_3 = r'C:\projects\dashboards_dash\data\gender_state_1.png'
encoded_image_3 = base64.b64encode(open(image_filename_3, 'rb').read()).decode('utf-8')  

layout = html.Div(children=[
    html.H1(children='Chi Square Test'),
    html.Img(src='data:image/png;base64,{}'.format(encoded_image),style={'display':'inline-block'}),
    html.Img(src='data:image/png;base64,{}'.format(encoded_image_1),style={'display':'inline-block'}),
    html.H1(children ="        "),
    
    html.Img(src='data:image/png;base64,{}'.format(encoded_image_2),style={'display':'inline-block'}),
    html.Img(src='data:image/png;base64,{}'.format(encoded_image_3),style={'display':'inline-block'}),
    dcc.Link('next', href='/page9')

])

