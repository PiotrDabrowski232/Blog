from django.contrib import admin
from .models import Uzytkownik, Post, Komentarz, ElementGraficzny


admin.site.register(Uzytkownik)
admin.site.register(Post)
admin.site.register(Komentarz)
admin.site.register(ElementGraficzny)
