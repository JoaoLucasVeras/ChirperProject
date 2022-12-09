# Project Name: Chirper
Simple Twitter replica app created with Flask, SQL, Bootstrap

## Authors
- Joao Lucas veras (@JoaoLucasVeras) - Team Lead
- Choyee Chan Myae (@ChoyeeMyae)
- Romuz Abdulhamidov (@Rha02)
- Tan Dao (@TanDao01262000)


### Table of Contents
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Setup](#setup)
* [Status](#status)

### Introduction
Chirper app is a social networking website where user can post messages known as "chirps". User can interact with other users by following them. User can also update their bio and nickname through edit profile. Chirper can be used on the mobile or pc with internet connection. 

### Technologies
Project is created with the following packages:

* certifi            2022.9.24
* charset-normalizer 2.1.1
* click              8.1.3
* dnspython          2.2.1
* email-validator    1.3.0
* Flask              2.2.2
* Flask-Login        0.6.2
* Flask-SQLAlchemy   3.0.2
* Flask-WTF          1.0.1
* greenlet           2.0.1
* idna               3.4
* importlib-metadata 5.0.0
* itsdangerous       2.1.2
* Jinja2             3.1.2
* MarkupSafe         2.1.1
* mysqlclient        2.1.1
* pip                22.3.1
* python-dotenv      0.21.0
* requests           2.28.1
* setuptools         41.2.0
* SQLAlchemy         1.4.44
* urllib3            1.26.13
* Werkzeug           2.2.2
* WTForms            3.0.1
* zipp               3.10.0

### Setup
- Install python. Must have 64-bit python 3 installed
- Install the required packages
- Create an environment file (`.env`) inside the repo (outside the app folder).

Populate the `.env` file with the following values:
```
DB_CONNECTION="admin01@chirperdb:chirper-admin22@chirperdb.mysql.database.azure.com:3306/app"
SECRET_KEY="NeverGonnaGiveYouUpNeverGonnaLetYouDown"
OPENWEATHER_API_KEY="b3a26bdb8d20554fb7b2157c6a32695b"
MAP_KEY="79Cato3BXsCCQ0YOvlYj"
```

To launch the application locally, run the following command:
```
py run.py
```
### Functional Requirements
1. Login (Joao)
2. Logout (Romuz)
3. Create New Account (Tan)
4. Delete Account (Choyee)
5. User Home Page (Joao)
6. Send Messages to Followers (Romuz)
7. Follow Users (Tan)
8. Search Users (Choyee)
9. Post Images with Message (Joao)
10. Connect with External API (Romuz)
11. Users Profile (Tan)
12. Authentication (verified) (Choyee)
### Non-functional Requirements
1. Using elements from Bootstrap (Jaoa)
2. Date format shall follow month-day-year (Choyee)
3. Dark Mode (Tan)
4. Responsive UI (Romuz)

### Status
We have implemented 11 functonal requirements so far except for #9.





