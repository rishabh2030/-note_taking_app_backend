run:
	@python manage.py runserver

makemigrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

createsuperuser:
	@python manage.py createsuperuser