# books/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
