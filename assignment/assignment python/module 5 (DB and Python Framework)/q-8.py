# #8] 

# # >>>
# # Make Django application to demonstrate following things o There will be 2 modules(Admin,Product manager) o Admin can add product name (ex.Product id and product name) ex. (1, Samsung), (2, Apple)...etc. Data should store in

# Create Django Project and App:First, create a Django project and then create a Django app within it.

# django-admin startproject product_project .
# python manage.py startapp product_app



# # Define Models:-

# from django.db import models

# class Admin(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return self.username

# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.product_name


# # Register Models in Admin:-

# from django.contrib import admin
# from .models import *

# admin.site.register(Admin)
# admin.site.register(Product)


# # Run Migrations

# python manage.py makemigrations
# python manage.py migrate


# #create superuser

# python manage.py createsuperuser


# # Run Server:

# python manage.py runserver

