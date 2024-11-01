from django.contrib import admin
from .models import UserProfile, Todo

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_number', 'age', 'created_at']

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'is_completed', 'created_at']
