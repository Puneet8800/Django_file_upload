# File Upload

### Instructions to run

- Install python3. On MacOS:
```
brew install python3
```
- Run:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install django-searchable-encrypted-fields
$ sudo pip install django-throttle-requests
$ python manage.py migrate
$ python manage.py runserver
```

- Visit http://localhost:8000/.

Functionality :
1. We can upload document and can view them.
2. We can download the uploaded document.
3. We can delete the uploaded document.
4. Whitlisted the file extension, can see the list in validators.py
5. For security measures, There is a rate limit on upload and delete functionality.
6. Backend database used: Sqlite.


Sample Image:
![alt text](https://github.com/Puneet8800/Django_file_upload/blob/master/example.png?raw=true)
