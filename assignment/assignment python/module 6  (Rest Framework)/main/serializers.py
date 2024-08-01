
from rest_framework import serializers
from .models import Book, Author, Publisher

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'publisher']
