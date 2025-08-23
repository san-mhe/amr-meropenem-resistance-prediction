# AMR Meropenem Resistance Prediction using Genomic Features

This project predicts **Antimicrobial Resistance (AMR)** to **Meropenem** in *Klebsiella pneumoniae* using machine learning (Random Forest & XGBoost), explains predictions with SHAP, and annotates top genetic features using the **CARD (Comprehensive Antibiotic Resistance Database)**.

> Interactive SHAP dashboard built with Dash. Fully reproducible ML pipeline with annotated gene output.

---

## Background

**Antimicrobial Resistance (AMR)** is a rising global health crisis, where bacteria evolve to resist antibiotics. Meropenem is a last-line drug against *Klebsiella pneumoniae*. Early detection of resistance can help benefit in drug delivery.

---

## Dataset

- Source: [Kaggle - AMR Resistant Klebsiella Genomes](https://www.kaggle.com/datasets/arashnic/amr-resistant-klebsiella-genomes)
- Samples: ~1,500 *Klebsiella* isolates
- Features: ~20,000+ k-mer binary indicators (presence/absence)
- Target: Meropenem Resistance → **0 (Susceptible), 1 (Resistant)**

---

## ⚙Pipeline Overview

```text
1. Load & clean genes data
2. Train Random Forest & XGBoost models
3. Extract SHAP values for top predictive k-mers
4. Annotate top SHAP features using CARD ontology
5. Visualize SHAP + gene annotations in Dash app for XG Boost Model
