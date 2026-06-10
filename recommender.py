from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from data_loader import load_data

# load cleaned data
df2 = load_data()

# import CountVectorizer and create the count matrix
count = CountVectorizer(stop_words = "english")
count_matrix = count.fit_transform(df2["soup"])

# compute the Cosine Similarity matrix based on the count_matrix
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# reset index of our main DataFrame and construct reverse mapping
df2 = df2.reset_index()
indices = pd.Series(df2.index, index = df2["title"])

# function that takes in the movie title as input and outputs the most similar movies
def get_recommendations(title):
    # validate movie title
    title = title.title()

    if title not in indices:
        return ["Movie not found. Please try another title."]

    # get movie index
    idx = indices[title]

    # get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)

    # get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    recommendations = []

    for movie_index, similarity_score in sim_scores:
        movie_title = df2["title"].iloc[movie_index]

        similarity_percent = round(similarity_score * 100, 2)

        recommendations.append(f"{movie_title} ({similarity_percent}% match)")

    return recommendations

