from django.contrib import admin
from .models import course, Content, Assignment, Quiz

# Register your models here.
admin.site.register(course)
admin.site.register(Content)
admin.site.register(Assignment)
admin.site.register(Quiz)

