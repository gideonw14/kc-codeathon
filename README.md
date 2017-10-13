# django-starter
A Django starter pack with user authentication set up
test

__Getting Started__
- PyCharm IDE - [Download](https://www.jetbrains.com/pycharm/download/#section=windows)
    - Community edition is fine, students get pro version free
- Python 3.6 [Download](https://www.python.org/downloads/)
- Python virtual environment - [Tutorial](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
    - NOTE: I highly recommend giving your virtual environment the prefix of `env` just to keep things clear
    
    - __PyCharm Method__
        - File > Settings > Project > Project Interpreter
        - Click on the small gear
        - Choose `Create VirtualEnv`
        - Give it a nice name
        - It will automagically install the dependencies listed in requirements.txt
            - If it doesn't just run `pip install -r requirements.txt` in the built in terminal
    
    - __IDE Independant Method__
        - Install virtualenv: `pip install virtualenv`
        - Install virtualenvwrapper for Windows: `pip install virtualenvwrapper-win`
        - Make a new virtual environment wrapper for the project
            - cd into the project
            - run command `mkvirtualenv env-<name>`
            - in your project dir run `workon env-<name>`
            - install dependencies with `pip install -r requirements.txt`
    
- Postgres - [Download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
    - Once downloaded, open PgAdmin and make a database that will be used by the project
    - Now you can run migrations to create the database. See steps below in *Useful Commands*
    - Note: The default port for Postgres is `5432`. I changed the port to `5431` for myself 
    so that it would not collide with another instance of Postgres. Be sure your 
    `DATABASES['PORT']` is the correct number.
- Set up environment variables for DEV_SECRETs - see settings files - [Tutorial](https://www.computerhope.com/issues/ch000549.htm)
    - `DEV_SECRET_1` is the `SECRET_KEY` variable in the settings - [Generator](https://www.miniwebtool.com/django-secret-key-generator/)
    - `DEV_SECRET_2` is the password for the database
    - `DEV_SECRET_3` is the password to the email server login

---

__Useful commands__

- NOTE: in order to see any errors associated with these commands, you must use `python` before `manage.py`
- NOTE: These commands are run in the repository folder - the one with `manage.py`.
- Start the server - `C:\...\project>manage.py runserver`
- Migrations - 2 step process - do this every time you make a change to the "database" or any `models.py` files.
1. `manage.py makemigrations` 
2. `manage.py migrate`
- Run automated tests - `C:\...\vigor-billing>manage.py test` 
    - optional: append `app-name` to only run tests for a specific app
- Crete a super user with admin capabilities- `C:\...\vigor-billing>manage.py createsuperuser`
- Django Shell - `C:\...\vigor-billing>manage.py shell`
- Export your dependencies to requirements.txt - `pip freeze > requirements.txt`
- Drop a trace anywhere in the code with `import ipdb; ipdb.set_trace()` to debug.

__Useful Docs__
- [Django](https://docs.djangoproject.com/en/1.11/)
- [Crispy Forms](http://django-crispy-forms.readthedocs.io/en/latest/)
- [Better Forms](http://django-betterforms.readthedocs.io/en/latest/multiform.html)
- [Guardian](https://django-guardian.readthedocs.io/en/stable/)
