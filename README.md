django-pos
A point of sale system implemented in django.

Setup
Clone this project.
git clone https://github.com/parthsharma2/django-pos.git
Move into the cloned project's directory.
cd django-pos
Create a python 3 virtual environment and activate it.
python3 -m venv env
source env/bin/activate
Install the requirements.
pip install -r requirements.txt
Make database migrations.
python manage.py makemigrations
python manage.py migrate
Run the application.
python manage.py runserver
