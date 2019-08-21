import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
sns.set(style="whitegrid")
#%matplotlib inline
    

def call_my_pickles():
    with open ('my_pickles/merged_data.p', 'rb') as readfile:
        merged_data = pickle.load(readfile)
    with open ('my_pickles/genres_df.p', 'rb') as readfile:
        genres_df = pickle.load(readfile)
    with open ('my_pickles/directors_by_profit_oscars.p', 'rb') as readfile:
        directors_by_profit_oscars = pickle.load(readfile)
    with open ('my_pickles/nominations.p', 'rb') as readfile:
        nominations = pickle.load(readfile)
    with open ('my_pickles/tmdb_cleaned.p', 'rb') as readfile:
        tmdb_cleaned = pickle.load(readfile)
    with open ('my_pickles/genres_names.p', 'rb') as readfile:
        genres_names = pickle.load(readfile)
    with open ('my_pickles/actors.p', 'rb') as readfile:
        actors = pickle.load(readfile)
    return (merged_data, genres_df, directors_by_profit_oscars, nominations, tmdb_cleaned, genres_names, actors)

def plot_profit_by_genre(genres_df):
    genres_df.sort_values(by = ['profit'], inplace = True, ascending = False)
    plt.figure(figsize = (15,8))
    sns.barplot(x = 'genre', y = 'profit', data = genres_df, color = 'crimson')
    plt.title('\nMean Profit by Genre\n', fontsize = 18)
    plt.ylabel('Mean Profit in Millions of Dollars\n', fontsize = 16)
    plt.xticks(rotation=60, fontsize = 16)
    plt.xlabel('Genre', fontsize = 16)
    plt.xticks(fontsize = 16)
    plt.show()
    return

def plot_oscar_comedydrama_directors(directors_by_profit_oscars):
    plt.figure(figsize = (15,8))
    plt.scatter(x = directors_by_profit_oscars.index, y = directors_by_profit_oscars['profit'], \
                s = (directors_by_profit_oscars['nominations']**1.)*1000, color = 'crimson')
    plt.ylim(90, 350)
    plt.xlim(-1,10)
    plt.xticks(rotation=50, fontsize = 14)
    plt.xlabel('Director', fontsize = 14)
    plt.title('\nOscar-Nominated Comedy/Drama Directors\' Average Film Profit\n', fontsize = 16)
    plt.ylabel('Average Profit / Film\n (millions of dollars)', fontsize = 14)
    plt.show()
    return


def plot_oscar_nominations_by_genre(genres_df):
    genres_df.sort_values(by = ['oscar_nominations'], ascending = False, inplace = True, )
    plt.figure(figsize = (15,8))
    sns.barplot(x = 'genre', y = 'oscar_nominations', data = genres_df, color = 'crimson')
    plt.xticks(rotation=60, fontsize = 16)
    plt.xlabel('Genre', fontsize = 16)
    plt.ylabel('Oscar Nominations \n', fontsize = 16)
    plt.title('\nNumber of Oscar Nominations by Genre\n', fontsize = 18)
    plt.show()
    return

def plot_actors(actors):
    actors_plot = []
    profits_plot = []
    for actor in actors:
        actors_plot.append(actor[0])
        profits_plot.append(actor[1])
        
    plt.figure(figsize = (15,6))
    sns.scatterplot(x = actors_plot, y = profits_plot, color = 'crimson')
    plt.xticks(rotation=80)
    plt.xlabel('Actor')
    plt.ylabel('Mean Profits in Millions of Dollars \n (per movie actor starred in)')
    plt.title('Profits Drama/Comedy Actors Bring on Average Per Film \n')
    plt.show()
    return

