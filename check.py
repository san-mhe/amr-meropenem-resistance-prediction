import pandas as pd

from annotate_genes_from_aro import annotated_df

aro_df = pd.read_csv("data/aro.tsv", sep='\t')

print(aro_df.columns.tolist())

shap_df = pd.read_csv("data/top_shap_genes_xgb.csv")
print(shap_df.columns.tolist())

ano_df = pd.read_csv("data/annotated_shap_genes_xgb.csv")
print(annotated_df.columns.tolist())

