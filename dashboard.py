from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

app = Dash()

df = pd.read_csv('dataset/retail_data.csv')
df.dropna(inplace=True)
df_10 = df.head()

app.layout = [
    html.Div(children='My First App with Data'),
    html.Hr(),
    html.Br(),
    # Data table
    dash_table.DataTable(data=df_10.to_dict('records'), page_size=10),
    # Simple graph   
    dcc.Graph(figure=px.histogram(df, x='Country', y='Amount', histfunc='sum'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)