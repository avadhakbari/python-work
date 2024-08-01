# 5] What is a QuerySet?Write program to create a new Post object in database: 

# >>>
# In Django, a QuerySet is a collection of objects from a database. It's a way to retrieve data from a database and manipulate it in Python. 
# QuerySets are lazy, meaning they don't actually retrieve the data from the database until you iterate over them or convert them to a list. 
# This allows you to define a query, and then refine it further before actually executing it.

# models.py (assuming you have a Post model defined)
# from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

# # Create a new Post object
# from.models import Post

# new_post = Post(title="My New Post", content="This is my new post content")
# new_post.save()