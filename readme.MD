# Created a time-entry application in Django.
● As a user, able to register with my name, username, email, etc.
● As a user,ble to log my time entries for a task with the following fields.
○ Input field to enter task name.
○ Start time and end time.
○ A timer which I can start to track time for a task.
● As a user, I should be able to browse through my time entries of previous days.


# requirements

python==3.6.9
django==3.0.5


# admin/
username = admin
password = admin


# To run 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver