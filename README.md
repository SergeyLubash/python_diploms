<h1 align="center">Hi š, I'm Sergey Lubash</h1>
<h3 align="center">A passionate backend developer from Russia</h3>

- š­ Iām currently working on [Todolist](slubash.ga)

- š± Iām currently learning **Django,Postgresql**

<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

Features
Imagine that you are working at Google, in the direction of calendar development ā calendar.google.com . Your Calendar app provides opportunities to work with meetings.

The following functions are implemented in the project:

Login/registration/authentication via vkontakte.
Creating goals. 2.1 Selecting the time interval of the goal with the number of days to complete the goal displayed. 2.2 Selecting a category of goals (personal, work, development, sports, etc.) with the ability to add/remove/update categories. 2.3 Goal priority selection (static list of minor, major, critical, etc.). 2.4 Goal completion status selection (in progress, completed, overdue, archived).
Change of goals. 3.1 Changing the goal description 3.2 Status change. 3.3 Give the opportunity to change the priority and category of the goal. 3.4 Deleting a goal. 3.4.1 When deleted, the goal changes its status to "archived".
Search by the name of the goal.
Filtering by status, category, priority, year.
Uploading goals in CSV/JSON.
Notes to goals.
All the listed functions must be implemented in Telegram bot
Tech
Prepare the project and configure all the necessary system components for further work.

Creating an application.

You need to install Django latest version (Django==4.0.1).
pip install Django==4.0.1 2. Create a project.

django-admin startproject to do list 3. Create a Git repository in GitHub.

Add a file.gitignore in the repository, you can use a ready-made template for python: https://github.com/github/gitignore/blob/main/Python .gitignore.

Send the files created in the Git repository to GitHub.

Do not forget to record your actions in the README file in parallel with writing the code Configure dependencies.

Create a virtual environment.

Add the created virtual environment to the project.

Activate the virtual environment.

Add a file requirements.txt in the root of the project, it will store all the dependencies that will be used in the project. The first dependency will be Django.

The contents of the file looks like this:

requirements.txt
Django==4.0.1 5. Install the dependencies specified in the file requirements.txt:

pip install -r requirements.txt Configure the configuration file. The configuration file is needed in order to configure the operation of the application for different environments (local and production). For example:

Debug mode should be enabled locally, but it should never be left enabled in production due to security and performance considerations. The database on the local computer and production will be located at different addresses, etc. We will configure the application using environment variables. To work with environment variables, you need to select a library. I recommend using:

https://github.com/joke2k/django-environ You can choose the python-dotenv library or any other.

Create a .env file in which to store the default settings.

In todolist/settings.py need to add library support and migrate parameters SECRET_KEY and DEBUG to the configuration file.

Variable ALLOWED_HOSTS assign a value ["*"] Implement registration

We will use Django REST Framework (DRF) to write the API.

You need to put DRF and add it to the dependencies (requirements.txt ) indicating the version. In the Core app, add urls.py and in the file todolist/urls.py enable urls from the Core application. Add a file serializers.py in the Core application. Describe Model Serializer for registration. The following points should be taken into account: you need to check the password strength using the built-in verification in Django; accept password and password_repeat and check if they match; do not store the password in its original form, but save the hash from it; do not create two users with the same username (users with the same email are allowed). Describe the View for user registration and add it to core/urls.py . When writing a View, you need to consider the following: the method must be accessible to unauthorized users; you can use Create API View as the base View. Implement login/password login

You have already faced the task of authenticating users using a jwt token. In this task, it is necessary to implement an alternative user authorization mechanism.

To log in, we will use cookies and the django.contrib.auth standard library to work with authorization in Django.

Cookies are a dictionary that the client (browser) sends with any HTTP request to the server. The server can add a new key to this dictionary or delete it. Upon successful user authentication, the server will set the session ID key, which can be used to determine which user accesses the server during the following requests. The session ID can be, for example: a jwt token or a unique string that is stored in the database and points to the user.

The logic of the method is as follows:

Get username and password from the user. Using the django.contrib.auth.authenticate mechanism to check the correctness of username/password. https://docs.djangoproject.com

In case of incorrect username/password, return an authorization error. If the username/password is correct, "remember" the user using django.contrib.auth.login and return the user object. https://docs.djangoproject.com

The functionality of the program The graphical user interface for working with goals is a board, where each goal is a card on this board.

Board The board is divided into 3 columns by status. On each card you can see. Sorting, filtering and search functions. Working with a goal Clicking on the card opens the detailed view of the goal screen. On it , the user can:

See detailed information about the goal. Edit the goal. Archive the target. Work with comments. Interface for categories There is a separate interface for working with categories:

Creating a category. Editing a category. View the list of categories. Deleting a category. Special deletion scenario Your product manager really asks that when deleting entities, they are not completely deleted, but remain in the database, while they would be hidden for the user. You discussed the behavior when deleting various entities and came to the conclusion:

When deleting a category: The category is marked as deleted and is no longer visible to the user. All goals included in the category are marked with the status "Archived". Deleting a goal = archiving a goal (there is no "Delete goal" button). You decided to leave the deletion of comments as is, and when you delete them, they are really erased from the database. Admin panel Portal administrators should be able to view all created entities. Each entity should have its own section inside which you can view/edit/delete entities.

So, we have discussed all the necessary functionality, now we are designing a database and highlighting the main entities:

Category. Goal. Comment on the goal. After we have decided on the database architecture, we will start planning the API.

Necessary methods For each entity we will need methods:

to create an entity; view a list of entities ā with the ability to search, filter and sort; editing an entity; viewing a specific entity; deleting an entity. Safety It is necessary to take into account the basic filtering ā the user should be able to see only what he created himself. It is also necessary to take this rule into account when creating/editing/deleting, for example:

The user should not be able to create goals in other people's categories, create comments on other people's goals. The user should be able to edit and delete only their goals/categories/comments.

Create a bot that requires account confirmation in the written application and through which you can receive and create goals.