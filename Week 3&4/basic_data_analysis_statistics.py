import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns

# Load the Iris dataset
data = sns.load_dataset('iris')

# One-Hot encode categorical columns (converts text to numbers for correlation analysis)
data_encoded = pd.get_dummies(data, columns=['species'])
print("Data after one-hot encoding:")
print(data_encoded.head())

# 1. EXPLORE THE DATA

# Print the first few rows
print("\nFirst few rows:")
print(data_encoded.head())

# Check data types
print("\nData types:")
print(data_encoded.info())

# Get summary statistics
print("\nSummary statistics:")
print(data_encoded.describe())

# 2. CALCULATE BASIC STATISTICS

# Get numerical columns
numerical_cols = data_encoded.select_dtypes(include=[np.number]).columns.tolist()

# Calculate mean, median, mode, and standard deviation for each numerical feature
for col in numerical_cols:
    print(f"\n{col}:")
    print(f"Mean: {data_encoded[col].mean():.3f}")
    print(f"Median: {data_encoded[col].median():.3f}")
    print(f"Mode: {stats.mode(data_encoded[col], keepdims=True)[0][0]:.3f}")
    print(f"Standard Deviation: {data_encoded[col].std():.3f}")

# Calculate correlation between features (numerical columns only)
print("\nCorrelation matrix:")
print(data_encoded[numerical_cols].corr()) 