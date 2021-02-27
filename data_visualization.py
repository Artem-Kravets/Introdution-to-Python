import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

exec(open('get_stock_data.py').read())
exec(open('get_crypto_currencies_data.py').read())
exec(open('data_preprocessing.py').read())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df_stocks = pd.read_csv('data/stocks/Stocks.csv')
df_cryptos = pd.read_csv('data/cryptos/Cryptos.csv')
#df_sectors = pd.read_csv('data/sector/Sectors.csv')

fig_stocks = px.line(df_stocks, x='timestamp', y='volume', color='name')
fig_stocks.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig_cryptos = px.line(df_cryptos, x='timestamp', y='volume', color='name')
fig_cryptos.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Python Dash App',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='by Artem Kravets', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Tabs([
        dcc.Tab(label='Stocks', children=[
            dcc.Graph(
                id='stocks',
                figure=fig_stocks
            ),
            dash_table.DataTable(
                id='stocks_table',
                columns=[
                    {"name": i, "id": i} for i in df_stocks.columns
                ],
                data=df_stocks.to_dict('records'),
                editable=True,
                filter_action="native",
                style_filter={'backgroundColor': '#7FDBFF'},
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current=0,
                page_size=13,
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(30, 30, 30)'
                    }
                ],
                style_cell={
                    'backgroundColor': '#111111',
                    'color': '#7FDBFF',
                    'textAlign': 'center',
                    'fontSize:': 16
                },
                style_header={
                    'backgroundColor': '#7FDBFF',
                    'fontWeight': 'bold',
                    'color': "black"
                },
            ),
            html.Div(id='datatable-interactivity-container'),
        ]),
        dcc.Tab(label='Crypto currencies', children=[

            dcc.Graph(
                id='cryptos',
                figure=fig_cryptos
            ),
            dash_table.DataTable(
                id='cryptos_table',
                columns=[
                    {"name": i, "id": i} for i in df_cryptos.columns
                ],
                data=df_cryptos.to_dict('records'),
                editable=True,
                filter_action="native",
                style_filter={'backgroundColor': '#7FDBFF'},
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current=0,
                page_size=13,
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(30, 30, 30)'
                    }
                ],
                style_cell={
                    'backgroundColor':  colors['background'],
                    'fontSize': 16,
                    'color': colors['text'],
                    'textAlign': 'center'
                },
                style_header={
                    'backgroundColor': colors['text'],
                    'fontWeight': 'bold',
                    'color': colors['background']


                },
            ),
            html.Div(id='cryptos_table_container'),
        ]),
    ])
])

if __name__ == '__main__':

    app.run_server(debug=False)
