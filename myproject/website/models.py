from django.db import models
from django.contrib.auth.models import User


class SocialAccount(models.Model):
    ICONS = [
        ("fa-facebook-f", "Facebook"),
        ("fa-instagram", "Instagram"),
        ("fa-google-plus-g", "Google+"),
        ("fa-linkedin-in", "Linkedin")
    ]

    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials account'

    def __str__(self):
        return self.nom



class SiteInfo(models.Model):
    map_url = models.TextField()
    email = models.EmailField()
    logo = models.ImageField(upload_to="images/SiteInfo")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Site info'
        verbose_name_plural = 'Site infos'

    def __str__(self):
        return self.email


class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length = 150)
    sujet = models.CharField(max_length = 150)
    email = models.EmailField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom, self.email



class Temoignage(models.Model):
    auteur = models.CharField(max_length=200)
    message = models.TextField()
    metier = models.CharField(max_length = 150)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

    def __str__(self):
        return str(self.auteur)


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/User", default='images/avatar.png', blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAccounts'

    def __str__(self):
        return str(self.user)

class Newlatters(models.Model):
    email = models.EmailField()
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Newlatters'
        verbose_name_plural = 'Newlatters'

    def __str__(self):
        return str(self.email)



