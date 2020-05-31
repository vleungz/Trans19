# Trans19

## Introduction
Trans-19 was developed to manage records of patients affected by COVID-19 and their visited locations. It allows users to enter, edit and delete records, search through them and view the data in table format. CHP staff logs in using their username and password, then, according to their status, access different functions of the system. Staff identified as Epidemiologists are able to identify connections between patients for the purpose of contact tracing. 

## Usage
- Change into project directory
cd comp3297proj

- Make virtual environment
mkvirtualenv trans19

- Install requirements
pip install -r requirements.txt

- Start the development server
python manage.py makemigration
python manage.py runserver

## Log in information
username: groupg

password: comp3297trans19

## Deployment
The project is deployed in Heroku http://trans19-g.herokuapp.com
