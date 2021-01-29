import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


df1 = pd.read_csv('monthly_adjusted_IBM.csv')
df1["name"] = "IBM"
df2 = pd.read_csv('monthly_adjusted_AAPL.csv')
df2["name"] = "APPLE"

df3 = pd.concat([df1, df2])
df3.to_csv("Stocks.csv")
df = pd.read_csv("Stocks.csv")

fig = px.line(df, x='timestamp', y="volume", color="name")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


def generate_table(dataframe, max_rows=15):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ], style={'marginLeft': 'auto', 'marginRight': 'auto', 'color': colors['text']})


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

    dcc.Graph(
        id='graph',
        figure=fig
    ),

    html.H4(children='Table', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    generate_table(df)

])

if __name__ == '__main__':
    app.run_server(debug=True)
