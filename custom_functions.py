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
    plt.yticks(fontsize = 16)
    plt.xticks(rotation=60, fontsize = 16)
    plt.xlabel('Genre', fontsize = 16)
    plt.xticks(fontsize = 16)
    plt.show()
    return

def plot_oscar_dramaadventure_directors(directors_by_profit_oscars):
    directors_by_profit_oscars.reset_index(inplace = True)
    plt.figure(figsize = (20,12))
    z = directors_by_profit_oscars['nominations'].values
    y = directors_by_profit_oscars['profit'].values
    n = directors_by_profit_oscars['director'].values
    plt.scatter(x = z, y = y, s = 4000, color = 'crimson', alpha = .7)
    for i, txt in enumerate(n):
        plt.annotate(txt, (z[i], y[i]), fontsize = 18, fontweight = 'bold', color = 'black')
    plt.title('\nProfit and Oscar Nominations for Drama/Adventure Directors\n', fontsize = 22)
    plt.xlabel('\nNumber of Oscar Nominations', fontsize = 16, fontweight = 'bold')
    plt.xticks(range(0,12),fontsize = 16)
    plt.ylabel('Mean Profit per Film \n(millions of dollars)\n', fontsize = 16, fontweight = 'bold')
    plt.yticks(fontsize = 16)
    plt.xlim(0,12)
    plt.ylim(100, 600)
    plt.show()       
    return

def plot_oscar_nominations_by_genre(genres_df):
    genres_df.sort_values(by = ['oscar_nominations'], ascending = False, inplace = True, )
    plt.figure(figsize = (15,8))
    sns.barplot(x = 'genre', y = 'oscar_nominations', data = genres_df, color = 'crimson')
    plt.xticks(rotation=60, fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.xlabel('Genre', fontsize = 16)
    plt.ylabel('Oscar Nominations \n', fontsize = 16)
    plt.title('\nProfit and Oscar Nominations for Drama/Adventure Directors\n', fontsize = 22)
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
    sns.barplot(x = actors_plot, y = profits_plot, color = 'crimson')
    plt.xticks(rotation=80, fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.xlabel('Actor', fontsize = 12)
    plt.ylabel('Mean Profits in Millions of Dollars \n (per movie actor starred in)', fontsize = 12)
    plt.title('Profits Drama/Adventure Actors Bring on Average Per Oscar-Nominated Film \n', fontsize = 14)
    plt.ylim(350,700)
    plt.show()
    return

