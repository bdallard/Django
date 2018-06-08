# Django Project presentation 
Here find my Django internship project for my final year in engineering school. 

## Getting started

Clone this repository.

## Running the app

Install a virtualenv. 
`$sudo pip install virtualenv`

To actually work inside a virtualenv, you need to enable it first. This is done by sourcing `bin/activate` inside your virtualenv folder.
`$ source VIRTUAL/bin/activate`

Installing Python packages after enabling your virtualenv. 
`$pip install -r requirements.txt`

Make migrations 
`$ python manage.py makemigrations && python manage.py migrate `

Collect static files 
`$ python manage.py collectstatic`

After that, run the app using Django manage.py.

`$python manage.py runserver`

Access the homepage on `http://localhost:8000`
