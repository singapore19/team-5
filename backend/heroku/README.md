# I love 2 write codes

### Setup
You'll need a .env file to pass environment variables to the application.
Ask it from someone :D

- (If you're creating a pipenv in WSL Ubuntu 18.04...)
```
pipenv install --python=`which python3`
```
- Install dependencies from Pipfile
```
pipenv install
```
- Run the pipenv shell
```
pipenv shell
```
- Serving the application with flask
```
flask run
```
- Serving the application with gunicorn
Note - there is no hot reloading with this method
```
gunicorn --bind 0.0.0.0:5000 app:app
```
