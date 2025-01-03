# FastAPI

Contenido del curso
- Path Operations
- Validaciones de datos
- Documentación
- Tipos de respuestas y códigos de estados
- Middlewares
- Dependencias
- Modularización
- Manejo de errores
- Y mucho más

Create a Virtual Environment
$ python -m venv .venv
$ source .venv/bin/activate
$ .venv\Scripts\activate  windows


fastapi dev main.py

$ pip install fastapi uvicorn

runapp
uvicorn main:app
uvicorn main:app --host localhost --port 5000 --reload

