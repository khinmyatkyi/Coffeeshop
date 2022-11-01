# coffeeshop
To create Virtual Environments
==============================
- Create New folder (eg. TestProject)
- in cmd (terminal) -> Go to path of TestProject folder exist
- enter following commend in terminal
          - python -m venv .venv

Activate Virtual Environment
===============================
- enter following commend in terminal 
       -In Window OS
	- .venv/scripts/activate
      -(or) In Max OS 
	- source .venv/bin/activate

Install the Django code
=====================
- pip install Django

To create Django Project
========================
- django-admin startproject coffeeshop
- cd coffeeshop

To create Django Admin User
==========================
- python manage.py createsuperuser
- enter your username, email, password and retype password

To create Django App
===========================
- python manage.py startapp api
- python manage.py startapp frontend
- python manage.py startapp menu

To make Migration
==========================================
- pip install pillow
- python manage.py makemigrations 
- python manage.py migrate

To run Django Server
=======================
- python manage.py runserver
