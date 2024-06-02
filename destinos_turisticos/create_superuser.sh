#!/bin/sh

# Variables de entorno para el superusuario
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=123456

# Ejecutar el comando createsuperuser sin interacción
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD') if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() else print('Superusuario ya existe.')"
