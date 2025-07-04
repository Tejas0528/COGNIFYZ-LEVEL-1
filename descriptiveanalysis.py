import pandas as pd

df = pd.read_csv("Dataset .csv")


print("\n Descriptive Statistics (Numerical Columns):")

numerical_cols = ['Votes', 'Aggregate rating', 'Price range'] 
for col in numerical_cols:
    if col in df.columns:
        print(f"\n {col}")
        print(f"Mean: {df[col].mean():.2f}")
        print(f"Median: {df[col].median():.2f}")
        print(f"Standard Deviation: {df[col].std():.2f}")
    else:
        print(f"\n Column '{col}' not found in the dataset.")

if 'Country Code' in df.columns:
    print("\n Distribution of Country Code:")
    print(df['Country Code'].value_counts())
else:
    print("\n 'Country Code' column not found.")


if 'City' in df.columns:
    print("\n Distribution of City:")
    print(df['City'].value_counts())
else:
    print("\n 'City' column not found.")

if 'Cuisines' in df.columns:
    df['Primary Cuisine'] = df['Cuisines'].astype(str).apply(lambda x: x.split(',')[0].strip())
    print("\n Distribution of Primary Cuisine:")
    print(df['Primary Cuisine'].value_counts())
else:
    print("\ 'Cuisines' column not found.")

if 'Primary Cuisine' in df.columns:
    print("\n Top 10 Cuisines with Most Restaurants:")
    print(df['Primary Cuisine'].value_counts().head(10))

if 'City' in df.columns:
    print("\n Top 10 Cities with Most Restaurants:")
    print(df['City'].value_counts().head(10))