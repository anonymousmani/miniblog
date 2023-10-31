from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class post_admin(admin.ModelAdmin):
    list_display = ('id', 'title' )

'''class contact_admin(admin.ModelAdmin):
    list_display = ('name',)'''

