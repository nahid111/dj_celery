# Using celery with django
<hr/>

[following the doc](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)

## Getting Started
1. clone the repo & cd into it.
2. Create a virtual environment for installing dependencies: 
<br/><nbsp/>`python3 -m venv project_name_venv`
3. Source the virtual environment:
<br/><nbsp/>`source project_name_venv/bin/activate`
4. Install the dependencies in the virtual environment: 
<br/><nbsp/>`pip install -r requirements.txt`

## Running the app
- Run redis in docker: 
```shell
docker run -d -p 6379:6379 --name mq redis
```
- Running the Celery worker server
```shell
celery -A dj_celery worker --loglevel=INFO
```
- Run the server: 
```shell
python manage.py runserver
```


