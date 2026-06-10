import tkinter as tk
from recommender import get_recommendations
from data_loader import load_data
from visualizations import (popularity_chart, genre_chart, ratings_scatterplot)

df = load_data()

# create basic window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("750x600")

# add title
title_label = tk.Label(root, text="Movie Recommendation System", font = ("Arial", 18))
title_label.pack(pady = 10)

# add search label and input box
label = tk.Label(root, text = "Enter Movie Title:")
label.pack(pady = 10)

movie_entry = tk.Entry(root, width = 40)
movie_entry.pack(pady = 5)

# add results box
results_box = tk.Listbox(root, width = 60, height = 15)
results_box.pack(pady = 20)

# connect recommendation button to function
def recommend_movies():
    movie_title = movie_entry.get()

    recommendations = get_recommendations(movie_title)

    # clear previous results
    results_box.delete(0, tk.END)

    # display recommended movies
    for movie in recommendations:
        results_box.insert(tk.END, movie + "\n")

# add recommendation button
recommend_button = tk.Button(root, text = "Get Recommendations", command = recommend_movies)
recommend_button.pack(pady = 10)

# visualization buttons
popularity_button = tk.Button(root, text = "Show Popularity Chart", command = lambda: popularity_chart(df))
popularity_button.pack(pady = 5)

genre_button = tk.Button(root, text = "Show Genre Chart", command = lambda: genre_chart(df))
genre_button.pack(pady = 5)

scatterplot_button = tk.Button(root, text = "Show Ratings Scatterplot", command = lambda: ratings_scatterplot(df))
scatterplot_button.pack(pady = 5)

print("Switch to Movie Recommendation window!")
root.mainloop()

