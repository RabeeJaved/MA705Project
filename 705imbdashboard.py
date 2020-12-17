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


url = 'https://github.com/RabeeJaved/MA705Project/blob/main/movieDataset.csv'
movieD = pd.read_csv(url, sep=',')

movieDF = movieDF.drop(columns= ['ImageURL', 'Synopsis'])


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
    


