from django.contrib import admin
from .models import *

# Register your models here.

class post_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc')

class contact_admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'message')

admin.site.register(Post, post_admin)
admin.site.register(contact, contact_admin)

