.PHONY: runserver try

.DEFAULT_GOAL := runserver

runserver:
	python manage.py runserver 8000

all-migrations:
	python manage.py makemigrations && python manage.py migrate
