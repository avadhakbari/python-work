from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)