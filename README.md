# kc-codeathon MST Team Miners 1
Our project for the 2017 Federal Reserve Coding Competition

Gideon Walker, Michael Ward, Eli Gaitley, and Levi Anderson

__Video Demonstration__

[Presentation Video](https://www.youtube.com/watch?v=Of2gb3npvD4)

__Problem__

The problem for this Code-a-Thon was to make an application that 
would help college students transition from college life to corporate life.

__Our Project__

Our main goal for this project was to make a web application that would 
allow a user to simulate being in a team project. Our big idea was to create
a game that allows multiple users to work together in a simulated 'project' where
 they would be required to perform a series of tasks that could have dependencies
 on other tasks. The users would be able to communicate
through an online chat room built in to the game. The users would then be required
to work together in order to divide up the project tasks and complete the project 
on time. The users would be able to play different games where each game would 
emphasize an aspect of working in corporate life, such as teamwork, leadership,
and communication. 

__More About the Game__

Each task has a category, duration, and dependencies. For a task to be available to 
start, the previous dependant tasks must be completed. Also, each player only has 
8 hrs. in a day for tasks, so the player must choose one or more tasks in which
the durations add to 8 hrs. There are cases where a player may be waiting on a 
dependant task or tasks to be complete, in which case they can 'study' a specific
category. Studying allows a player to reduce the amount of time required to
complete a task of that category. 

One idea we had to make the game more interesting/realistic was to add random
events that could occur in the project environment that would affect the 
players, usually negatively. For example, a team member might be sick and not
able to work that day, or if they do come in to work they will take longer
to complete tasks and have a chance to get other team members sick.

__What we accomplished__

We recognized from the beginning that communication would be a very important
aspect of a multiplayer version of our game. This was one of our first goals
was to get chat room functionality added to our website. We did accomplish
this feature, but we were not able to integrate it into the game. As time
started growing short, we decided to focus our energy on creating the game 
mechanics. We also realized that it would be very difficult to make a multiplayer
game in the time allotted so we focused on making our game single player first. 
The game we decided to make is called 'office simulator'. The player is trying
to design and build furniture for a client. We were able to implement the 
task view that shows the player all of the tasks they have to complete. The player
can then click on a task and it will show up in the 'Tasks to do Today' list. 
Once the user selects 8 hrs. of tasks to fulfill, they can submit their tasks and
it will update the game state. 

__Disclaimers__

- We used the Django Web framework to build our web app.
- We already had user authentication set up before the codeathon started
- For the chat rooms we integrated an example chat room into our project 
 from https://github.com/andrewgodwin/channels-examples.

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
