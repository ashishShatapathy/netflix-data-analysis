import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("netflix_titles.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# -------------------------------
# Data Cleaning
# -------------------------------
print("\nMissing Values in Dataset:")
print(df.isnull().sum())

df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# -------------------------------
# Movies vs TV Shows
# -------------------------------
type_counts = df['type'].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(x=type_counts.index, y=type_counts.values)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# -------------------------------
# Top Countries Producing Content
# -------------------------------
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

# -------------------------------
# Content Added Over Time
# -------------------------------
df['year_added'] = df['date_added'].dt.year
year_counts = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
year_counts.plot(kind='line')
plt.title("Netflix Content Added Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# -------------------------------
# Top Genres Analysis
# -------------------------------
genres = df['listed_in'].str.split(',').explode()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.show()

# -------------------------------
# Top Directors Analysis
# -------------------------------
directors = df['director'].str.split(',').explode()
top_directors = directors.value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_directors.values, y=top_directors.index)
plt.title("Top Directors on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.show()