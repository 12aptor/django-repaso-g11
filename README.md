# Crear una aplicacion con Django

## Crear un entorno virtual

```bash
python -m venv venv
```

## Activar el entorno virtual

```bash
source venv/bin/activate
```

## Instalar Django

```bash
pip install django
```

## Crear un proyecto

```bash
django-admin startproject mysite
```

## Acceder al proyecto

```bash
cd mysite
```

## Crear una aplicacion

```bash
python manage.py startapp myapp
```

## Agregar la aplicacion al proyecto

```python
# mysite/settings.py

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'myapp',
]
```

## Crear una base de datos

```bash
python manage.py migrate
```

## Crear un super usuario

```bash
python manage.py createsuperuser
```

## Correr el servidor

```bash
python manage.py runserver
```

## Crear un modelo

```python
from django.db import models

class MyModel(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

## Crear una migracion

```bash
python manage.py makemigrations
```

## Aplicar una migracion

```bash
python manage.py migrate
```

## Registrar el modelo en el admin

```python
from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description', 'created_at', 'updated_at')

admin.site.register(MyModel)
```
