# -*- coding: utf-8 -*-
"""TCGA_BRCA_TP53_Expression_vs_Mutation_Analysis

## Step 1: Load and Inspect Gene Expression Data (Transcriptomics )

This dataset contains log2(FPKM + 1) normalized gene expression values for TCGA-BRCA samples.
Each row represents a gene, and each column represents a sample ID (TCGA barcode).

We will:
- Load the dataset using `pandas`
- Preview the shape and gene/sample identifiers
- Check if our gene of interest (*TP53*) is included
"""

# Import required library
import pandas as pd

# Load the expression data
df_expr = pd.read_csv("TCGA-BRCA.star_fpkm.tsv.gz", sep ="\t", index_col=0)

# Preview of shape of the expression matrix
print("The shape of expression matrix: ", df_expr.shape) # (Ensembl IDs x samples)

# Show first few rows
df_expr.head()

"""### Step 1B: Locate TP53 in Expression Matrix

The expression matrix uses Ensembl gene IDs instead of gene symbols like TP53.

To extract TP53 expression:
- Find its Ensembl ID (`ENSG00000141510`)
- Locate that row in the expression matrix

"""

# Find all rows containing TP53
tp53_rows = [i for i in df_expr.index if "ENSG00000141510" in i]

# View TP53 expression values across samples
df_expr.loc[tp53_rows].T.head()  # Transpose for readability

"""### Step 1C: Clean and Rename TP53 Expression Data

We convert the TP53 expression row to a DataFrame and rename it for clarity.

- This improves interpretability
- Makes merging and plotting easier

"""

# Convert to DataFrame for merging later
tp53_expr_df = df_expr.loc[tp53_rows].T  # transpose to make samples rows
tp53_expr_df.columns = ["TP53_Expression"]
tp53_expr_df.index.name = "Sample_ID"
tp53_expr_df.reset_index(inplace=True)

# Save as a table
tp53_expr_df.to_csv("TP53_expression_table.tsv", sep="\t", index=False)

tp53_expr_df.head()

"""## Step 2: Load and Filter Mutation Data (Genomics Layer)

We load the TCGBRCA somatic mutation file.  
Then we filter for samples where the gene TP53 is mutated, and extract their barcodes.

We'll use this to label samples as:
- 'Mutated' if TP53 is altered
- 'Wild-type' if TP53 is not mutated

"""

# Load mutation data
df_mut = pd.read_csv("TCGA-BRCA.somaticmutation_wxs.tsv.gz", sep="\t")

# Preview columns
print("Mutation data columns: ", df_mut.columns.tolist())

# Preview first few rows
df_mut.head()

# Filter rows where the mutated gene is TP53
df_tp53_mut = df_mut[df_mut["gene"]== "TP53"]

# Get unique sample barcodes that have TP53 mutation
mutated_samples = df_tp53_mut["sample"].unique()
print("Number of samples with TP53 mutation:", len(mutated_samples))
pd.Series(mutated_samples).head()

"""## Step 3: Label Samples as "Mutated" or "Wild-type"

Now that we have the TP53-mutated sample list, we label each sample in our TP53 expression dataset.

- If a sample is found in the mutated list → label as "Mutated"
- Otherwise → label as "Wild-type"

"""

# Create mutation status column
tp53_expr_df["Mutation_Status"] = tp53_expr_df["Sample_ID"].apply(
    lambda x: "Mutated" if x in mutated_samples else "Wild-type")

# Check counts
tp53_expr_df["Mutation_Status"].value_counts()

tp53_expr_df.head(10)

"""## Step 4: Export the Final Multi-Omics Dataset

This dataset includes TP53 expression values and mutation status for all TCGA-BRCA samples.

We will save it as a `.csv` file for use in R for visualization.

"""

# Save the final dataframe to CSV for statistical analysis and visualization in R
tp53_expr_df.to_csv("TP53_expression_mutation_status.csv", index=False)

print("File saved successfully!")

