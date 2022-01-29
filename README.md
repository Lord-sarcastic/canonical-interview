This service, built with Python, is one that provides access to an audit log of events that have taken place within a system of microservices.

Task details can be accessed [here](/task.md).


## Technologies used
- Server application:
    - [Django](https://www.djangoproject.com/), A Python web framework with focus on speed of development and perfectionism
    - [Django Rest Framework](https://www.django-rest-framework.org/), A sub-package for creating REST APIs with Django
    - [PostgreSQL](https://www.postgresql.org/), an open source object-relational database system.
    - [Postman](https://www.getpostman.com/), a complete API development environment, and flexibly integrates with the software development cycle for API testing.

## Installation
 - Prerequisites:
    - Python 3.9
    - PostgreSQL

- Basic installation:
    - Install [Python](https://www.python.org/downloads/) and [PostgreSQL](https://www.postgresql.org/) on your host environment (or PC).
    - Install [Pipenv](https://pipenv.pypa.io/en/latest/) using `pip3 install pipenv`.
    - Create a Postgres database with an appropriate name. Note the host, port, username and password of the database. Ensure the database is running.
    - Ensure Git is installed, then clone this repository by running `git clone https://github.com/Lord-sarcastic/canonical-interview.git` in the terminal.
    - Enter the directory with `cd canonical-interview`
    - Create a `.env` file using the [.env.example](/.env.example) file as a template. Ensure to fill in appropriate values. The `APP_HOST` variable refers to the domain host you'll be running this app on.
    - Run `pipenv install` to install all necessary dependencies for the server application in a virtual environment.
    - Run `pipenv shell` to activate the virtual environment.
    - Run `python manage.py migrate` to run migrations to create database tables
    - Optionally, you can create a superuser account to access the Django admin with `python manage.py createsuperuser`.
    - Run the server with `python manage.py runserver`. It should be running on port 8000.

## API Enpoints documentation
Database schema:
![](/sql-diagram.png)

It can also be viewed in SQL form [here](/schema.sql)
The application is made up of a single route which is quite simple to use and embodies lots of functionalities including creating the required resources, retrival and filtering as needed.

- `POST /api/v1/events/` -> Log an entry from a microservice
- `GET /api/v1/events/` -> Retrieve previously logged entries.

## Testing 🚨
- Test using browsable API form by visiting the route `/api/v1/events/`
- Testing with Postman
    - Install [Postman](https://www.getpostman.com/) or any preferred REST API Client such as [Insomnia](https://insomnia.rest/), [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client), etc.
    - Get the application up and running by following the instructions in the Installation Guide of this README.
Use the [API documentation](https://documenter.getpostman.com/view/10277419/UVeCQTai) as a guide to access available endpoints.

## Discussion
This section contains justifications and improvements that should be made.

### Choice of Database
Whilst PostgreSQL has been chosen for this project, a better choice would have been a NoSQL database as they generally are more performant as write-heavy, read-seldom databases.

### Flexibility
Given that we may have newer event types in future, it is important that the entries are as flexible as possible, so a consistent and universal log level is defined for services to make use of, with `INFO` more or less a default most likely defined by the microservice involved itself.

The crux of flexibility is in `event_action`, `event_metadata` and `event_data`.
- Event action: This defines the type of action carried out by the microservice. Using an enum in place of a separate table is more or less a tradeoff, as other actions may be defined in future. Enums are chosen to ensure consistency across service, with a fallback option, `OTHER` provided for services that do not have an appropriate action listed so far. In the case of insistence of specifying a custom action, we are led to the next field:
- Event metadata: An optional field containing additional information specified by the service. Here, a microservice could add fields and be as flexible and customized as it should be without being constained by other fields that makes use of Enums for specifying data types.
- Event data: This should not be confused with the meta data field, as this has to do with the data being interacted upon or being engaged in a request.

## Licence 🔐
[MIT licensed](/LICENSE) © [Ayodeji Adeoti](https://github.com/Lord-sarcatic)

## Credits 🙏
- Half of the Open Source Software community who contribute to the whole of the tools I use
- Guido Van Rossum, that pretty Python guy
- Others who would be thanked by my smiles and Quora tags