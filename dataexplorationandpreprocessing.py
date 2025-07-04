import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Dataset .csv")

print("\n Dataset Shape:")
print(f"Number of rows: {len(data)}")
print(f"Number of columns: {len(data.columns)}")

print("\n🧹 Missing Values (before handling):")
print(data.isnull().sum())

data = data.dropna(subset=['Aggregate rating'])

data['Cuisines'] = data['Cuisines'].fillna('Not Specified')
data['City'] = data['City'].fillna('Unknown')
data['Votes'] = data['Votes'].fillna(0)
data['Price range'] = data['Price range'].fillna(data['Price range'].mode()[0])

print("\n Missing values handled.")

print("\n Data Types Before:")
print(data.dtypes)

data['Votes'] = data['Votes'].astype(int)
data['Price range'] = data['Price range'].astype(int)

print("\n Data Types After Conversion:")
print(data.dtypes)

print("\n Target Variable: Aggregate Rating Distribution")
rating_counts = data['Aggregate rating'].value_counts().sort_index()
print(rating_counts)

plt.figure(figsize=(8, 5))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette='pastel')
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.show()

print("\n Class Imbalance Check:")
total = rating_counts.sum()
for rating, count in rating_counts.items():
    percentage = (count / total) * 100
    print(f"Rating {rating}: {count} restaurants ({percentage:.2f}%)")