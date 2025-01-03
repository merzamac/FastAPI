from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()
# Aplicando modelo de datos
class Movie(BaseModel):
	#id: Optional[int] = None
	id: int
	title:str
	overview:str
	year:str
	rating:float
	category:str

class MovieUpdate(BaseModel):
	title:str
	overview:str
	year:str
	rating:float
	category:str

#app.title = "Mi primera aplicacion"
#app.version = "2.0.0"

movies = [
	{
		"id":1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llosado Pandora viven los Na'vi, seres que ....",
		"year": 2009,
		"rating": 7.8,
		"category": "Accion"
	},
	{
		"id":2,
		"title": "Batman",
		"overview": "En un exuberante planeta llosado Pandora viven los Na'vi, seres que ....",
		"year": 2009,
		"rating": 7.8,
		"category": "Comedia"
	}
]

@app.get('/',tags=['Home'])
def home():
	return "hola world"

# uso del get
@app.get('/movies',tags=['Movies'])
def get_movies() -> List[Movie]:
	return movies

# parametros de rutas
@app.get('/movies/{id}',tags=['Movies'])
def get_movies(id: int) -> Movie:
	for movie in movies:
		if movie['id'] == id:
			return movie

	return []

# parametros query
@app.get('/movies/',tags=['Movies'])
def get_movies_by_category(category: str,year:int) -> Movie:
	for movie in movies:
		if movie['category'] == category and movie['year'] == year:
			return movie
	return []

# metodo post
"""@app.post('/movies',tags=['Movies'])
def create_movie(
	id:int = Body(), 
	title:str = Body(), 
	overview:str = Body(), 
	year:int = Body(),
	rating:float = Body(),
	category:str = Body()):
	movies.append(
		{
		'id':id,
		'title': title,
		'overview': overview,
		'year':year,
		'rating': rating,
		'category': category
		}
		)
	return movies"""

#Usando el esquema de la clase
@app.post('/movies',tags=['Movies'])
def create_movie(movie:Movie) -> List[Movie]:
	movies.append(movie.model_dump())
	return movies


"""@app.put('/movies/{id}',tags=['Movies'])
def update_movie( 
		id:int,
		title:str = Body(), 
		overview:str = Body(), 
		year:int = Body(),
		rating:float = Body(),
		category:str = Body()
	):

	for movie in movies:
		if movie['id'] == id:
			movie['title'] = title
			movie['overview'] = overview
			movie['year'] = year
			movie['rating'] = rating
			movie['category'] = category

	return movies"""
@app.put('/movies/{id}',tags=['Movies'])
def update_movie( id:int,movie:MovieUpdate)-> List[Movie]:

	for item in movies:
		if item['id'] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category

	return movies

@app.delete('/movies/{id}',tags=['Movies'])
def delete_movie(id:int) -> List[Movie]:
	for movie in movies:
		if movie['id'] == id:
			movies.remove(movie)
	return movie
