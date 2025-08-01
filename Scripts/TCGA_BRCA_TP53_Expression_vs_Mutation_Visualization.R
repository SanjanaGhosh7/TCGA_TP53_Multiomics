### Step 1: Load required libraries
library(ggplot2)
library(readr)   # For reading CSV files

### Step 1A: Set working directory 
setwd("C:/Users/sanja/TCGA_multiomics_project")

### Step 1B: Read the final merged dataset
df <- read.csv("TP53_expression_mutation_status.csv")
# Preview the data
head(df)


### Step 2: Create the Plot(Violin Plot )
ggplot(df, aes(x = Mutation_Status, y = TP53_Expression, fill = Mutation_Status)) +
  geom_violin(trim = FALSE, alpha = 0.6) +
  geom_boxplot(width = 0.1, outlier.shape = NA, alpha = 0.8) +
  labs(title = "TP53 Expression in Mutated vs Wild-Type BRCA Samples",
       x = "Mutation Status",
       y = "log2(FPKM + 1)") +
  theme_minimal() +
  theme(legend.position = "none")

# Save the plot
ggsave("tp53_violin_plot.pdf", width = 7, height = 7)


### Step 3: Statistical Comparison in Python

#Welch's t-test was used to compare TP53 expression between Mutated and Wild-type BRCA samples.

#A significant difference (p < 0.05) was observed, indicating that mutation status may influence TP53 expression levels.

# Run unpaired t-test
t_test_result<- t.test(TP53_Expression ~ Mutation_Status, data = df)
print(t_test_result)
