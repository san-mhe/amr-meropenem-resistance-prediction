import pandas as pd

#XG Boost Model Specific
#Load top SHAP genes file
shap_df = pd.read_csv("data/top_shap_genes_xgb.csv")

#Load the ARO TSV retrieved from CARD Ontology

aro_df = pd.read_csv("data/aro.tsv", sep="\t")

#Merge using the appropriate column(The columns and dataframe from CARD ARO file were checked inside check.py and aligned)
#Match SHAP gene names (column 'Gene' with ARO 'Name')
merged_df = pd.merge(shap_df, aro_df, left_on="Feature", right_on="Name", how="left")


#Create a new DataFrame with selected and renamed columns

annotated_df = merged_df[[
    "Feature",
    "Mean_SHAP_Value",
    "Accession",
    "Description",
    "CARD Short Name"
]].rename(columns={
    "Accession": "ARO Accession",
    "Description": "Resistance Mechanism",
    "CARD Short Name": "AMR Gene Family"
})

#Save the annotated file
annotated_df.to_csv("data/annotated_shap_genes_xgb.csv", index=False)

print("Saved to 'data/annotated_shap_genes_xgb.csv'")

