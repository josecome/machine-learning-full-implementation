# machine-learning-full-implementation
This project aims to demostrate how to build Machine Learning Pipeline, integrate it to backend and frontend Applications.

## To run the project
Machine Learning Pipeline
### Running Machine Learning Service
```sh
py run.py
```
or
```sh
flask --app hello run
```

Backend API (Django Rest Framework)
### Running Migrations
```sh
py manage.py makemigrations
py manage.py migrate
```
### Running Backend Application
```sh
py manage.py runserver
```

Frontend API (Vuejs)
## Project Setup
```sh
npm install
```
### Compile and Hot-Reload for Development
```sh
npm run dev
```
Server will run on [http://127.0.0.1:5173]
### Compile and Minify for Production
```sh
npm run build
```
