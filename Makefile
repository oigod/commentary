makemigrations:
	docker-compose exec app python manage.py makemigrations

migrate:
	docker-compose exec app python manage.py migrate

createsuperuser:
	docker-compose exec app python manage.py createsuperuser

collectstatic:
	docker-compose exec app python manage.py collectstatic --noinput

appshell:
	docker-compose exec -it app sh

dbshell:
	docker-compose exec -it db sh
