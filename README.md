https://youtu.be/qRJly5m2zJg

Key Constraints:
- stateless (you don't need to worry about state on server side)- Because REST is built that way
- Resourceful
- Client server architecture
- Layered System (Request -> Server -> DB) eg. Security Layer (logged in or not), then pass to next layer (logic)
- Cacheability (Can be intermediary layer, cache response of API to improve performance without passing through server)

Benefits:
- State is not required to store at server side
- Performance, Reliability
- Cross platform applications (Linux/Mac/Android/iOS)

Example:
    Endpoint of user resource
    localhost:8000/api/v1/user/1/
    GET, POST, DELETE, PUT

```
python3 -m virtualenv venv
source ./venv/bin/activate
```

- manage.py - interact with Django project
- init.py- This directory should be considered a Python package
- settings.py - conf for project
- urls.py - URL declaration for Django
- wsgi.py -  To serve your project



# Commands Used:
```
pip3 install django
pip3 install djangorestframework
django-admin --version
django-admin startproject quiz
python3 manage.py createsuperuser --email admin@admin.com --username admin
python3 manage.py makemigrations
python3 manage.py migrate

django-admin startapp qv1

Generate ERD:
brew install graphviz
pip3 install django-extensions
pip3 install pyparsing pydot
python3 manage.py graph_models -a > erd.dot
python3 manage.py graph_models -a > erd.dot && python3 manage.py graph_models --pydot -a -g -o erd.png 

```

