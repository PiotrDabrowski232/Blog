from django.db import models
from django.contrib.auth.models import User

class Uzytkownik(models.Model):
    nazwa_uzytkownika = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    haslo = models.CharField(max_length=100)
    rola = models.CharField(
        max_length=20, 
        choices=[
            ('Uzytkownik', 'Uzytkownik'), 
            ('Moderator', 'Moderator'), 
            ('Administrator', 'Administrator')
        ]
    )

    def __str__(self):
        return self.nazwa_uzytkownika

class Post(models.Model):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField(max_length=2000)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    DOSTEP_CHOICES = (
        ('Publiczny', 'Publiczny'),
        ('Ograniczony', 'Ograniczony'),
    )
    dostep = models.CharField(max_length=20, choices=DOSTEP_CHOICES, default='Publiczny')

    def __str__(self):
        return self.tytul

class Komentarz(models.Model):
    tresc = models.TextField()
    data_dodania = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Komentarz do {self.post.tytul}"

class ElementGraficzny(models.Model):
    url = models.URLField()
    opis = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Element graficzny dla {self.post.tytul}"
