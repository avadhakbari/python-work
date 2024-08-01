#4] What is Django URLs?make program to create django urls 

# >>>
# ----------
# myapp/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'), 
#     path('about/', views.about, name='about'),  
#     path('contact/', views.contact, name='contact'), 
# ]


# # myapp/views.py

# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Welcome to the home page!")

# def about(request):
#     return HttpResponse("This is the about page.")

# def contact(request):
#     return HttpResponse("Contact us at example@example.com")


# --------
# myproject/urls.py

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('myapp.urls')),  
# ]