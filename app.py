from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet_json():
    return {"Hello": "World!"}

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

#Load annotated data
df = pd.read_csv("./annotated_shap_genes_xgb.csv")

#Initialize Dash app
app = dash.Dash(__name__)
app.title = "AMR SHAP Dashboard"

#Layout (This step was adjusted using OpenAI ChatGPT 4o)

app.layout = html.Div([
    html.H1("Top SHAP Genes (XGBoost)", style={'textAlign': 'center'}),

    html.Label("Filter by Resistance Mechanism:", style={'marginTop': '20px'}),
    dcc.Dropdown(
        options=[{'label': m, 'value': m} for m in df['Resistance Mechanism'].dropna().unique()],
        id='mechanism-dropdown',
        placeholder='Select a resistance mechanism',
        style={'width': '80%', 'margin': '0 auto'}
    ),

    dcc.Graph(id='shap-bar-chart'),

    html.H3("Gene Details", style={'textAlign': 'center', 'marginTop': '40px'}),
    html.Div(id='details-table', style={'width': '95%', 'margin': '0 auto'})
])


#Callbacks
@app.callback(
    [Output('shap-bar-chart', 'figure'),
     Output('details-table', 'children')],
    [Input('mechanism-dropdown', 'value')]
)
def update_output(mechanism):
    if mechanism:
        filtered_df = df[df['Resistance Mechanism'] == mechanism]
    else:
        filtered_df = df

    fig = px.bar(
        filtered_df.sort_values("Mean_SHAP_Value", ascending=True),
        x="Mean_SHAP_Value", y="Feature", orientation='h',
        labels={"Feature": "Gene", "Mean_SHAP_Value": "SHAP Value"},
        title="Top SHAP Features"
    )
    fig.update_layout(template="simple_white", height=500)

    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtered_df.columns])),
        html.Tbody([
            html.Tr([html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns])
            for i in range(len(filtered_df))
        ])
    ], style={'marginTop': '20px'})

    return fig, table


#Run
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=7860)
