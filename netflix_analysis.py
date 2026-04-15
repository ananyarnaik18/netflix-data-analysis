import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

# Load dataset
df = pd.read_csv("netflix.csv")

print("First 5 rows:\n", df.head())

# -------------------------------
# 🔍 FILTERING
# -------------------------------

# Only Movies
movies = df[df["type"] == "Movie"]
print("\nMovies:\n", movies)

# Only TV Shows
tv_shows = df[df["type"] == "TV Show"]
print("\nTV Shows:\n", tv_shows)

# -------------------------------
# 📊 GROUPBY
# -------------------------------

# Count by Type
type_count = df.groupby("type")["show_id"].count()
print("\nCount by Type:\n", type_count)

# Top Countries
top_countries = df["country"].value_counts().head(5)

top_countries.plot(kind='bar', title="Top 5 Countries")
plt.show()

# Release Year Trend
year_count = df.groupby("release_year")["show_id"].count()
print("\nContent by Year:\n", year_count)

genres = df["listed_in"].value_counts().head(5)

genres.plot(kind='bar', title="Top Genres")
plt.show()

ratings = df["rating"].value_counts()

ratings.plot(kind='bar', title="Ratings Distribution")
plt.show()


# -------------------------------
# 📈 VISUALIZATION
# -------------------------------

# 1. Bar chart - Movies vs TV Shows
type_count.plot(kind='bar', title="Movies vs TV Shows")
plt.show()

# 2. Pie chart - Country distribution
country_count.plot(kind='pie', autopct='%1.1f%%', title="Country Distribution")
plt.show()

# 3. Line chart - Release trend
year_count.plot(kind='line', marker='o', title="Release Year Trend")
plt.show()