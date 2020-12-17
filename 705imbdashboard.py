'''
Created on Dec 16, 2020

@author: rabee
'''

import pandas as pd
import requests
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px



#Key1: "ac044f5f44mshf2818ed66358b97p1844adjsn5591556189aa"
#Key2: "800b59f9d4msh41d5a1000b99d1bp15204ejsnc44156d8194e"
#Key3: "5af1c543dcmshd675ff48f246eebp135993jsn88ae4ce5e9c0"
#Key4: "c42003b29amsh7ad231821ac0ab1p13247ajsndddb250c613e"


cols = ['IMDbID', 'Genre', 'Released', 'Title', 'IMDbRating', 'Type', 'Synopsis', 'ImageURL']
movieDF = pd.DataFrame(columns = cols)


# Dataframe year 2010-2014, Comedy

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2010, 
               "end_year": 2014,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "comedy",
               "sort": "highestrated",
               "language": "english",
               "no_of_votes": "2000"}

headers = {
    'x-rapidapi-key': "ac044f5f44mshf2818ed66358b97p1844adjsn5591556189aa",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movCom1 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movCom1 = movCom1.append([fulllist[n]], ignore_index=True)

movCom1 = movCom1.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})


# Dataframe year 2010-2014, Drama

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2010, 
               "end_year": 2014,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "drama",
               "sort": "highestrated",
               "language": "english",
               "no_of_votes": "2000"}

headers = {
    'x-rapidapi-key': "800b59f9d4msh41d5a1000b99d1bp15204ejsnc44156d8194e",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movDra1 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movDra1 = movDra1.append([fulllist[n]], ignore_index=True)

movDra1 = movDra1.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})


# Dataframe year 2010-2014, Action

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2010, 
               "end_year": 2014,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "action",
               "sort": "highestrated",
               "language": "english",
               "no_of_votes": "2000"}

headers = {
    'x-rapidapi-key': "5af1c543dcmshd675ff48f246eebp135993jsn88ae4ce5e9c0",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movAct1 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movAct1 = movAct1.append([fulllist[n]], ignore_index=True)

movAct1 = movAct1.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})



# Dataframe year 2010-2014, Thriller

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2010, 
               "end_year": 2014,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "thriller",
               "sort": "highestrated",
               "language": "english",
               "no_of_votes": "2000"}

headers = {
    'x-rapidapi-key': "c42003b29amsh7ad231821ac0ab1p13247ajsndddb250c613e",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movThr1 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movThr1 = movThr1.append([fulllist[n]], ignore_index=True)

movThr1 = movThr1.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})



#  --------------------------------------------------------------------

'''# Dataframe year 2015-2020, Comedy

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2015, 
               "end_year": 2020,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "comedy",
               "sort": "highestrated",
               "language": "english",
               "no_of_votes": "2000"}

headers = {
    'x-rapidapi-key': "ac044f5f44mshf2818ed66358b97p1844adjsn5591556189aa",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movCom2 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movCom2 = movCom2.append([fulllist[n]], ignore_index=True)

movCom2 = movCom2.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})



# Dataframe year 2015-2020, Drama

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2015, 
               "end_year": 2020,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "drama",
               "sort": "highestrated",
               "language": "english",
               "no_of_votes": "2000"}

headers = {
    'x-rapidapi-key': "800b59f9d4msh41d5a1000b99d1bp15204ejsnc44156d8194e",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movDra2 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movDra2 = movDra2.append([fulllist[n]], ignore_index=True)

movDra2 = movDra2.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})



# Dataframe year 2015-2020, Action

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2015, 
               "end_year": 2020,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "action",
               "sort": "highestrated",
               "language": "english",
               "votes": "2000"}

headers = {
    'x-rapidapi-key': "5af1c543dcmshd675ff48f246eebp135993jsn88ae4ce5e9c0",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movAct2 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movAct2 = movAct2.append([fulllist[n]], ignore_index=True)

movAct2 = movAct2.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})



# Dataframe year 2015-2020, Thriller

url = 'https://ott-details.p.rapidapi.com/advancedsearch'

querystring = {"start_year": 2015, 
               "end_year": 2020,
               "max_imdb": 9.5, 
               "type": "movie",
               "genre": "thriller",
               "sort": "highestrated",
               "language": "english",
               "no_of_votes": "2000"}

headers = {
    'x-rapidapi-key': "c42003b29amsh7ad231821ac0ab1p13247ajsndddb250c613e",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

movies = json.loads(response.text)

strires = movies["results"]
headers = ['imdbid', 'genre', 'released', 'title', 'imdbrating', 'type', 'synopsis', 'imageurl']
movThr2 = pd.DataFrame()


for each in strires:
    if 'imdbid' not in each:
        each['imdbid'] = ''
    if 'genre' not in each:
        each['genre'] = ''
    if 'released' not in each:
        each['released'] = ''
    if 'title' not in each:
        each['title'] = ''    
    if 'type' not in each:
        each['type'] = ''
    if 'synopsis' not in each:
        each['synopsis'] = ''
    if 'imageurl' not in each:
        each['imageurl'] = ''
    if 'imdbrating' not in each:
        each['imdbrating'] = ''
    
    else:
        continue

fulllist = []
for each in strires:
    appendedlist = []
    for col in headers:
        if col in each:
            appendedlist.append(str(each[col]))
        
    fulllist.append(appendedlist)

for n in range(0, len(strires)):
    movThr2 = movThr2.append([fulllist[n]], ignore_index=True)

movThr2 = movThr2.rename(columns= {0: 'IMDbID', 1: 'Genre', 2: 'Released', 3: 'Title', 4: 'IMDbRating', 5: 'Type', 6: 'Synopsis', 7: 'ImageURL'})



movCom1 = movCom1.append(movCom2)
movDra1 = movDra1.append(movDra2)
movAct1 = movAct1.append(movAct2)
movThr1 = movThr1.append(movThr2)'''

movieDF = movCom1
movieDF = movieDF.append(movDra1)
movieDF = movieDF.append(movAct1)
movieDF = movieDF.append(movThr1)


# CODE BEGINS:-

movieD = pd.read_csv('movieDataset.csv')
movieDF = movieD.drop(columns= ['ImageURL', 'Synopsis'])


for x in range(0, len(movieDF)):
    split = movieDF["Genre"][x].split("'")
    for genre in split:
        if genre.isalpha() == True:
            movieDF["Genre"][x] = genre



movieDF = movieDF.drop_duplicates()


# Type Graph:-
grouped = movieDF.groupby(['Released', 'Type']).size()
grouped = grouped.reset_index()

fig2 = px.bar(grouped, x = grouped['Released'], y = 0, color = 'Type', barmode = 'group')
fig2.update_layout(xaxis_title = 'Years',
                  yaxis_title = 'TotalMovies',
                  legend_title = 'Type',
                  )


# Genre Graph :-
pies = movieDF
pies['nGen'] = pies['Genre']

pies = pies.groupby(['Genre', 'nGen']).size()
pies.columns = ['Total']
pies = pies.reset_index()

fig3 = px.pie(pies, values = 0, names = 'Genre')
fig3.update_layout(legend_title = 'Genres')

movieDF = movieDF.drop(columns = ['nGen'])

'''   ------------------------------------------------------------------------- '''


stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



# pandas dataframe to html table

def generate_table(dataframe, max_rows=20):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)

server = app.server


app.layout = html.Div([
    html.H1('Welcome to Movie Recommendations Dashboard!', style={'textAlign': 'center'}),
    html.H3('This dashboard displays the highest rated movies since 2010, by year and genre', style={'textAlign': 'center'}),
    
    html.Img(src='https://www.goldenglobes.com/sites/default/files/articles/cover_images/2017-la_la_land.jpg',
             style={'height' : '30%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 50}),
    
    html.Img(src='https://m.media-amazon.com/images/M/MV5BNzQxNTIyODAxMV5BMl5BanBnXkFtZTgwNzQyMDA3OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
             style={'height' : '35%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 25}),
    
    html.Img(src='https://m.media-amazon.com/images/M/MV5BNGNiNWQ5M2MtNGI0OC00MDA2LWI5NzEtMmZiYjVjMDEyOWYzXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX182_CR0,0,182,268_AL_.jpg',
             style={'height' : '35%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 25}),
    
    html.Img(src='https://m.media-amazon.com/images/M/MV5BMGUwZjliMTAtNzAxZi00MWNiLWE2NzgtZGUxMGQxZjhhNDRiXkEyXkFqcGdeQXVyNjU1NzU3MzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
             style={'height' : '35%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 25}),
    
    html.Img(src='https://m.media-amazon.com/images/M/MV5BMjAyNDEyMzc4Ml5BMl5BanBnXkFtZTgwMjEzNjM0NTM@._V1_UX182_CR0,0,182,268_AL_.jpg',
             style={'height' : '35%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 25}),
    
    html.Img(src='https://m.media-amazon.com/images/M/MV5BZGVmY2RjNDgtMTc3Yy00YmY0LTgwODItYzBjNWJhNTRlYjdkXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX182_CR0,0,182,268_AL_.jpg',
             style={'height' : '35%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 25}),

    html.Img(src='https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
             style={'height' : '35%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 25}),

    html.Img(src='https://m.media-amazon.com/images/M/MV5BMjI0ODcxNzM1N15BMl5BanBnXkFtZTgwMzIwMTEwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
             style={'height' : '35%', 'width' : '10%', 'float' : 'center', 'position' : 'relative', 'padding-top' : 0, 'padding-left' : 25}),
    
    
    html.Br(),
    html.Br(),
    
    
    html.H5("Yearly Performance of Each Genre", style={'textAlign': 'center'}),
    dcc.Dropdown(options=[{'label': 'Action', 'value': 'Action'}, {'label': 'Comedy', 'value': 'Comedy'},
                          {'label': 'Drama', 'value': 'Drama'}, {'label': 'Documentary', 'value': 'Documentary'},
                          {'label': 'Romance', 'value': 'Romance'}, {'label': 'Thriller', 'value': 'Thriller'},
                          ],
                id = 'MultiGenre',
                multi = True,
                value = ['Drama', 'Comedy'],
                style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    dcc.Graph(id = 'MultiGenreGraph',
              style = {'width': '70%', 'float': 'center', 'padding-left' : 200}),
    
    
    html.Br(),
    html.Br(),
    
    
    html.H5("Highest Rated Movie(s) by: Year/Genre", style={'textAlign': 'center'}),
    dcc.Dropdown(options=[{'label': 'Year', 'value': 'Released'},
                          {'label': 'Genre', 'value': 'Genre'}],
                style={'width': '50%',
                       'margin-left': '284px',
                       'margin-bottom': '10px',
                       'verticalAlign': 'middle'},
                id='GenreYearDropdown',
                value='Year'),

    html.Div(id='GenreYearOutput',
             style={'margin-left' : '300px'}),
    
    html.Br(),
    html.Br(),
    
    html.Div([
        html.H5("Highest Rated Movies Released on TV versus in Theatres", 
            style={'display': 'inline-block', 'textAlign': 'center'}),
        html.Br(),
        dcc.Graph(id='TVMovieGraph', figure = fig2,
              style={'display': 'inline-block', 'float': 'left',})],
        
        style={'width': '49%', 'float': 'left'}),
    
    html.Div([
        html.H5("Genre Proportion of Most Popular Movies", 
            style={'display': 'inline-block', 'textAlign': 'center'}),
        html.Br(),
        dcc.Graph(id='GenrePieGraph', figure = fig3,
              style={'display': 'inline-block', 'float': 'right',})],
        
        style={'width': '49%', 'float': 'right'}),
    
    html.Br(),
    html.Br(),
    
    html.H5("Movie Averages per Genre, per Year", style={'textAlign': 'center'}),
    
    dcc.Checklist(options=[{'label': '2010', 'value': '2010'},
                           {'label': '2011', 'value': '2011'},
                           {'label': '2012', 'value': '2012'},
                           {'label': '2013', 'value': '2013'},
                           {'label': '2014', 'value': '2014'},
                           {'label': '2015', 'value': '2015'},
                           {'label': '2016', 'value': '2016'},
                           {'label': '2017', 'value': '2017'},
                           {'label': '2018', 'value': '2018'},
                           {'label': '2019', 'value': '2019'},
                           {'label': '2020', 'value': '2020'}],
                            
                            id = 'bar-slider',
                            value = ['2010', '2020'],
                            style={'margin-left' : '750px'}),
    
    html.Div(id = 'barhgraph',
             style={'margin-left' : '600px'})

])



@app.callback(
    Output(component_id='GenreYearOutput', component_property='children'),
    [Input(component_id='GenreYearDropdown', component_property='value')]
)
def GenreYearOutput(input_value):
    

    if input_value == 'Released':
        data = movieDF[movieDF.groupby('Released')['IMDbRating'].transform('max') == movieDF['IMDbRating']]
        data = data.sort_values(by = ['Released'])
        
    elif input_value == 'Genre':
        data = movieDF[movieDF.groupby('Genre')['IMDbRating'].transform('max') == movieDF['IMDbRating']]
        data = data.sort_values(by = ['Genre'])
    
    else:
        data = pd.DataFrame()
        
    return generate_table(data)



@app.callback(
    Output(component_id='MultiGenreGraph', component_property='figure'),
    [Input(component_id='MultiGenre', component_property='value')]
)
def GenreYearGraph(genres):
    
    if len(genres) < 1:
        movieDF1 = movieDF['Genre' == 'Drama']
        
    else:
        movieDF1 = movieDF[movieDF.Genre.isin(genres)]
    
    grouped_genre = movieDF1.groupby(['Released', 'Genre']).agg({'IMDbRating': ['mean']})
    
    grouped_genre.columns = ['AvgRating']
    grouped_genre = grouped_genre.reset_index()        
    
    fig = px.line(grouped_genre, x = grouped_genre['Released'], y = grouped_genre['AvgRating'], color = 'Genre')
    fig.update_layout(xaxis_title = 'Years',
                      yaxis_title = 'Avg Ratings',
                      legend_title = 'Genre')
    
    return fig



@app.callback(
    Output(component_id='barhgraph', component_property='children'),
    [Input(component_id='bar-slider', component_property='value')]
)

def BarGraph(year):
        
    movieGenres = movieDF.groupby(['Released', 'Genre']).agg({'IMDbRating': ['mean']})
    
    movieGenres.columns = ['AvgRating']
    movieGenres = movieGenres.reset_index()        
    
    
    year = list(year)
    newDF = movieGenres[movieGenres['Released'].isin(year)]
    
    return generate_table(newDF)


if __name__ == '__main__':
    app.run_server(debug=True)
    


