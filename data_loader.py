import pandas as pd
import numpy as np

from ast import literal_eval

# get the director's name and if not listed, return NaN
def get_director(x):
    for i in x:
        if i["job"] == "Director":
            return i["name"]
    return np.nan

# returns the list top 3 elements or entire list; whichever is more
def get_list(x):
    if isinstance(x, list):
        names = [i["name"] for i in x]
        # if more than 3 elements exist, return the first 3, if not return entire list
        if len(names) > 3:
            names = names[:3]
        return names

    # return empty list in case of missing/malformed data
    return []

# function to convert all strings to lower case and strip names of spaces
def clean_data(x):
    if isinstance(x,list):
        return [str.lower(i.replace(" ", ""))  for i in x]
    else:
        # check if director exists. if not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ""

# create metadata soup string which contains all the metadata
def create_soup(x):
    return " ".join(x["keywords"]) + " " + " ".join(x["cast"]) + " " + x["director"] + " " + " ".join(x["genres"])

def load_data():
    df1 = pd.read_csv("tmdb_5000_credits.csv")
    df2 = pd.read_csv("tmdb_5000_movies.csv")

    df1.columns = ["id", "credits_title", "cast", "crew"]
    df2 = df2.drop_duplicates()
    df2 = df2.merge(df1, on="id")

    # fill missing overview values
    df2["overview"] = df2["overview"].fillna("")

    features = ["cast", "crew", "keywords", "genres"]
    for feature in features:
        df2[feature] = df2[feature].apply(literal_eval)

    # extract director
    df2["director"] = df2["crew"].apply(get_director)

    # limit metadata list
    features = ["cast", "keywords", "genres"]
    for feature in features:
        df2[feature] = df2[feature].apply(get_list)

    # apply clean_data function to the features
    features = ["cast", "keywords", "director", "genres"]

    for feature in features:
        df2[feature] = df2[feature].apply(clean_data)

    # create metadata soup
    df2["soup"] = df2.apply(create_soup, axis=1)

    return df2
