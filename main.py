from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

#app.title = "Mi primera aplicacion"
#app.version = "2.0.0"

movies = [
	{
		"id":1,
		"titte": "Avatar",
		"overvier": "En un exuberante planeta llosado Pandora viven los Na'vi, seres que ....",
		"year": 2009,
		"rating": 7.8,
		"category": "Accion"
	},
	{
		"id":2,
		"titte": "Batman",
		"overvier": "En un exuberante planeta llosado Pandora viven los Na'vi, seres que ....",
		"year": 2009,
		"rating": 7.8,
		"category": "Comedia"
	}
]

@app.get('/',tags=['Home'])
def home():
	return "hola world"

# uso del get
@app.get('/movies',tags=['Home'])
def get_movies():
	return movies

# parametros de rutas
@app.get('/movies/{id}',tags=['Home'])
def get_movies(id: int):
	for movie in movies:
		if movie['id'] == id:
			return movie

	return []

# parametros query
@app.get('/movies/',tags=['Home'])
def get_movies_by_category(category: str,year:int):
	for movie in movies:
		if movie['category'] == category and movie['year'] == year:
			return movie

	return []
