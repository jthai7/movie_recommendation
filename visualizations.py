import matplotlib.pyplot as plt

def popularity_chart(df):
    # sort by popularity
    pop_movies = df.sort_values(by=['popularity'], ascending=False).head(10)

    plt.figure(figsize=(10,5))

    plt.barh(pop_movies["title"], pop_movies["popularity"])

    plt.gca().invert_yaxis()

    plt.xlabel("Popularity")

    plt.title("Top 10 Most Popular Movies")

    plt.tight_layout()

    plt.show()

def genre_chart(df):
    genre_counts = {}

    # count genres
    for genres in df["genres"]:
        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    # top 6 genres
    sorted_genres = sorted(genre_counts.items(), key = lambda x: x[1], reverse = True)[:6]

    labels = [x[0] for x in sorted_genres]

    sizes = [x[1] for x in sorted_genres]

    plt.figure(figsize = (7,7))

    plt.pie(sizes, labels = labels, autopct = '%1.1f%%')

    plt.title("Movie Genres")

    plt.show()

def ratings_scatterplot(df):
    plt.figure(figsize = (8,5))

    plt.scatter(df["vote_average"], df["popularity"])

    plt.xlabel("Vote Average")

    plt.ylabel("Popularity")

    plt.title("Movie Ratings vs Popularity")

    plt.tight_layout()

    plt.show()