import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data_path = 'C:\\Users\\hongj\\venv\\HR_anal\\data\\Expert_HR_data.csv'
data = pd.read_csv(data_path)

# Check the data types to see which columns need to be converted or handled
data_types = data.dtypes

# For correlation, convert categorical variables using one-hot encoding
data_numeric = pd.get_dummies(data, drop_first=True)

# Calculate correlations with PerformanceRating
correlations = data_numeric.corr()['PerformanceRating'].sort_values()

# Create a heatmap for visualization of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(data_numeric.corr(), annot=False, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

correlations, data_types

# Plotting the relationship between PercentSalaryHike and PerformanceRating
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['PercentSalaryHike'], y=data['PerformanceRating'], alpha=0.6)
plt.title('Scatter Plot of PercentSalaryHike vs. PerformanceRating')
plt.xlabel('Percent Salary Hike')
plt.ylabel('Performance Rating')
plt.grid(True)
plt.show()


