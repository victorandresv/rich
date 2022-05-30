# Rich - Orders API

### INSTALL DEPENDENCIES
````shell
pip install fastapi
pip install uvicorn
pip install requests
pip install gunicorn
````

### RUN DEVELOPMENT
````shell
uvicorn rich:app --reload
````

### DEPLOY TO SERVER
````shell
gunicorn -c gunicorn_conf.py rich:app
````