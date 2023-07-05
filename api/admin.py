from django.contrib import admin

from .models import Lesson

@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']