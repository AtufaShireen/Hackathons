from dash import Dash, dcc, html, Input, Output, callback

from year import page1 as year_page1
from year import page3 as year_page3

from age_group import page1 as age_page1
from age_group import page2 as age_page2
from age_group import page3 as age_page3
from age_group import page4 as age_page4

from type_cause import page1 as type_page1
from type_cause import page2 as type_page2
from type_cause import page3 as type_page3

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return app.layout
    if pathname == '/page1':
        return year_page1.layout
    elif pathname == '/page3':
        return year_page3.layout
    elif pathname == '/page4':
        return age_page1.layout
    elif pathname == '/page5':
        return age_page2.layout
    elif pathname == '/page6':
        return age_page3.layout
    elif pathname == '/page7':
        return age_page4.layout
    elif pathname == '/page8':
        return type_page1.layout
    elif pathname == '/page9':
        return type_page2.layout
    elif pathname == '/page10':
        return type_page3.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)