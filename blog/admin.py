from django.contrib import admin
from .models import Post

# Регистрация модели Post в административной панели
admin.site.register(Post)
