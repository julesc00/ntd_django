# Django REST API
Repository: [NTD API App](https://github.com/julesc00/ntd_django/tree/main)

## Dependencies
1. Install Pipenv: Start a terminal and run the following commands:  
```pip install --user pipenv```  
2. Install Django:  
```pipenv install django```  
Start environment:  ```pipenv shell```  
Run server: ```python manage.py runserver``` or ```./manage.py runserver```

## Prepare Database
1. Create a new database in SQLite:  
```python manage.py migrate```
2. Create a superuser:  
```python manage.py createsuperuser```


## Records import from GraphQL API
1. Once environment is activated and server is running, execute file `api/add_records.py`:  
```python api/add_records.py```