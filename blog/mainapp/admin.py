from django.contrib import admin
from .models import Uzytkownik, Post, Komentarz, ElementGraficzny

class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ('nazwa_uzytkownika', 'email', 'rola')
    list_filter = ('rola',)
    fieldsets = (
        (None, {'fields': ('nazwa_uzytkownika', 'email', 'haslo')}),
        ('Permissions', {'fields': ('rola',)}),
    )
    search_fields = ('nazwa_uzytkownika', 'email')
    ordering = ('nazwa_uzytkownika',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'data_utworzenia', 'autor', 'dostep')
    list_filter = ('dostep', 'autor', 'data_utworzenia')
    fieldsets = (
        (None, {'fields': ('tytul', 'tresc', 'autor', 'image', 'dostep')}),
    )
    search_fields = ('tytul', 'autor__username')
    ordering = ('-data_utworzenia',)

class KomentarzAdmin(admin.ModelAdmin):
    list_display = ('post', 'autor', 'data_dodania', 'tresc')
    list_filter = ('data_dodania', 'autor', 'post')
    fieldsets = (
        (None, {'fields': ('post', 'autor', 'tresc')}),
    )
    search_fields = ('post__tytul', 'autor__username', 'tresc')
    ordering = ('-data_dodania',)

class ElementGraficznyAdmin(admin.ModelAdmin):
    list_display = ('post', 'url', 'opis')
    list_filter = ('post',)
    fieldsets = (
        (None, {'fields': ('post', 'url', 'opis')}),
    )
    search_fields = ('post__tytul', 'url')
    ordering = ('post',)

admin.site.register(Uzytkownik, UzytkownikAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Komentarz, KomentarzAdmin)
admin.site.register(ElementGraficzny, ElementGraficznyAdmin)
