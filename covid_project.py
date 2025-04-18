import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel(r"C:\Users\basap\OneDrive\Desktop\python\month 2\covid_19.xlsx")
print("\ncolumn names:")
print(data.columns)
print("First 10 rows:")
print(data.head())
print("\nMissing Values:")
print(data.isnull().sum())
data = data.fillna(0)
print("\nAvailable columns:")
print(data.columns)
print("\nTotal Confirmed:", data['Confirmed'].sum())
print("Total Deaths:", data['Deaths'].sum())
print("Total Recovered:", data['Recovered'].sum())
top10 = data.groupby('country')['Confirmed'].sum().sort_values(ascending=False).head(15)
print("\nTop 10 Countries:")
print(top10)
top10.plot(kind='bar', color='skyblue')
plt.title('Top 15 Countries - Confirmed Cases')
plt.xlabel('Country')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()
print("\nData Preview:")
print(data.head())
print("\nAvailable columns:")
print(data.columns)