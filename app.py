import pandas as pd
import dash
from dash import dcc, html, dash_table, Input, Output
import plotly.express as px

#Load the annotated SHAP data (XG Boost Specific)
df = pd.read_csv("data/annotated_shap_genes_xgb.csv")

#Initialize Dash app
app = dash.Dash(__name__)
app.title = "XGBoost SHAP Explainability for AMR Genes"

#Layout (This step was adjusted using OpenAI ChatGPT 4o)

app.layout = html.Div([
    html.H1("Top SHAP Genes (XGBoost)", style={"textAlign": "center"}),

    html.Div([
        html.Label("Filter by Resistance Mechanism:"),
        dcc.Dropdown(
            id='mechanism-filter',
            options=[{'label': mech, 'value': mech} for mech in sorted(df['Resistance Mechanism'].dropna().unique())],
            placeholder="Select a resistance mechanism",
            clearable=True
        ),
    ], style={'width': '50%', 'margin': '0 auto'}),

    dcc.Graph(id='shap-bar'),

    html.H3("Gene Details", style={"textAlign": "center"}),
    dash_table.DataTable(
        id='gene-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        page_size=10
    )
], style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'})


#Callbacks
@app.callback(
    [Output('shap-bar', 'figure'),
     Output('gene-table', 'data')],
    [Input('mechanism-filter', 'value')]
)
def update_output(selected_mechanism):
    if selected_mechanism:
        filtered_df = df[df['Resistance Mechanism'] == selected_mechanism]
    else:
        filtered_df = df

    fig = px.bar(
        filtered_df.sort_values("Mean_SHAP_Value", ascending=False).head(20),
        x="Mean_SHAP_Value",
        y="Feature",
        orientation='h',
        title="Top SHAP Features",
        labels={"Mean_SHAP_Value": "SHAP Value", "Feature": "Gene"},
        height=600
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})

    return fig, filtered_df.to_dict('records')


#Run app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
