import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns

# Load the Iris dataset
data = sns.load_dataset('iris')

# 1. EXPLORE THE DATA

# Print the first few rows
print("First few rows:")
print(data.head())

# Check data types
print("\nData types:")
print(data.info())

# Get summary statistics
print("\nSummary statistics:")
print(data.describe())

# 2. CALCULATE BASIC STATISTICS

# Get numerical columns
numerical_cols = data.select_dtypes(include=[np.number]).columns.tolist()

# Calculate mean, median, mode, and standard deviation for each numerical feature
for col in numerical_cols:
    print(f"\n{col}:")
    print(f"Mean: {data[col].mean():.3f}")
    print(f"Median: {data[col].median():.3f}")
    print(f"Mode: {stats.mode(data[col], keepdims=True)[0][0]:.3f}")
    print(f"Standard Deviation: {data[col].std():.3f}")

# Calculate correlation between features
print("\nCorrelation matrix:")
print(data.corr())