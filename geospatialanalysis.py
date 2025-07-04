import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset .csv")

df = df.dropna(subset=['Latitude', 'Longitude', 'Aggregate rating', 'City', 'Country Code'])

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Longitude', 
    y='Latitude', 
    hue='Aggregate rating', 
    data=df,
    palette='coolwarm', 
    alpha=0.6,
    edgecolor='w',
    s=50
)
plt.title(' Restaurant Locations by Rating')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Rating', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n Top 10 Cities by Number of Restaurants:")
top_cities = df['City'].value_counts().head(10)
print(top_cities)

print("\n Top Countries by Number of Restaurants (using Country Code):")
top_countries = df['Country Code'].value_counts().head(10)
print(top_countries)

print("\n Correlation Between Location and Rating:")
corr_lat = df['Latitude'].corr(df['Aggregate rating'])
corr_lon = df['Longitude'].corr(df['Aggregate rating'])

print(f"Correlation between Latitude and Rating: {corr_lat:.4f}")
print(f"Correlation between Longitude and Rating: {corr_lon:.4f}")

plt.figure(figsize=(6, 4))
sns.heatmap(df[['Latitude', 'Longitude', 'Aggregate rating']].corr(), annot=True, cmap='viridis')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
