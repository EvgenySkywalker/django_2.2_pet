запуск
docker-compose up
docker exec -it django_22_pet-server-1 bash
python manage.py createsuperuser
http://127.0.0.1:8000/admin/ - Админ панель
http://127.0.0.1:8000/swagger/ - Swagger API
