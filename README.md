# 🧬 TCGA_TP53_Multiomics

**Author**: Sanjana Ghosh  
**Role**: Bioinformatics Postgraduate | Aspiring Genomics Data Scientist  
**Tools**: Python, R, Pandas, ggplot2, Jupyter, RStudio


---


## 📌 Project Title:

Exploring Gene Expression and Mutation Status in Breast Cancer using TCGA Multi-Omics Data.


---


## 🎯 Objective:

To gain hands-on experience in integrating genomic (mutation) and transcriptomic (expression) data from TCGA-BRCA and extract insights relevant to cancer subtyping and precision medicine.


---


## 📂 Data Source

- TCGA-BRCA Gene Expression data for TP53:  
  🔗 https://gdc-hub.s3.us-east-1.amazonaws.com/download/TCGA-BRCA.star_fpkm.tsv.gz
- TCGA-BRCA Gene Mutation data for TP53 is given in the `Data/` folder.


---


## 👩‍💻 Skills demonstrated: 
- Python scripting
- R visualization
- TCGA data integration
- somatic mutation analysis
- statistical testing 
- reproducible pipeline development
- Independent execution of an end-to-end multi-omics project
- Scientific reporting
- Demonstrated use of open-access cancer research data resources (TCGA, Xena)


---


## 1. 📌 Introduction

Breast cancer is a heterogeneous disease with distinct molecular subtypes. Integrating multi-omics data such as somatic mutations and gene expression is key to understanding tumor biology. This project focuses on the TP53 gene, a well-known tumor suppressor frequently mutated in breast cancer, and explores how its mutation status relates to its gene expression profile.


---


## 2. 🔍 Data Source and Tools

# Dataset: TCGA-BRCA multi-omics data downloaded from UCSC Xena

Mutation Data: TCGA-BRCA.somaticmutation_wxs.tsv.gz given in  `Data/` folder.

Expression Data: TCGA-BRCA.star_fpkm.tsv.gz (can be downloaded from the link given above).

# Tools Used:

- Python (Pandas) for data wrangling and integration.

- R (ggplot2, t.test()) for statistical analysis and visualization.

- Jupyter Notebook for Python scripting.

- RStudio for R scripting.


---


## 3. 🧪📊 Methodology

# Step 1: Expression Data Processing

Loaded the FPKM-normalized expression data.

Located Ensembl ID for TP53: ENSG00000141510.18

Extracted and transposed TP53 expression values across all samples.

# Step 2: Mutation Data Processing

Loaded somatic mutation data.

Filtered mutations for the TP53 gene.

Extracted unique TCGA sample barcodes with TP53 mutation.

Matched barcodes to expression data samples.

# Step 3: Data Integration

Merged expression and mutation datasets by sample ID.

Annotated each sample with mutation status: "Mutated" or "Wild-type".

# Step 4: Visualization

Created violin plot comparing TP53 expression between mutation groups.

# Step 5: Statistical Testing

Performed Welch's t-test to compare TP53 expression levels between mutated and wild-type samples.


---


## 4. 💡 Interpretation and Insight

Despite similar medians in the visual plots, Welch's t-test revealed a statistically significant downregulation of TP53 expression in the mutated group. This suggests possible transcriptional dysregulation or mRNA instability linked to TP53 mutations.


---


## 5. 💊 Relevance to Cancer Subtyping and Precision Medicine

- Cancer Subtyping: TP53 mutation and expression levels may inform molecular classification.

- Precision Medicine: Expression differences related to mutation status can support decisions regarding personalized treatment approaches.


---


## 6. 📓 Conclusion

This project demonstrates the value of integrating somatic mutation and gene expression data to uncover transcriptional consequences of mutations. It highlights how even basic statistical and visualization approaches can yield meaningful biological insights in cancer research.


---


## 7. 📂 Files and Deliverables

- Python scripts: TCGA_BRCA_TP53_Expression_vs_Mutation_Analysis.ipynb, tcga_brca_tp53_expression_vs_mutation_analysis.py

- R script: TCGA_BRCA_TP53_Expression_vs_Mutation_Visualization.R

- Final merged dataset: TP53_expression_mutation_status.csv

- Plot: tp53_violin_plot.png


---

## 8. 🚀 Future Scope

- Expand analysis to other tumor suppressors and oncogenes

- Include additional omics layers (e.g., copy number variation, methylation, immune infiltration)

- Correlate with clinical outcomes (e.g., survival analysis)


---

📬 Feel free to Connect or Collaborate

**Sanjana Ghosh**
[LinkedIn](www.linkedin.com/in/sanjana-ghosh-2a5b7c11d) | sanjanaghosh150@gmail.com
