from django.contrib import admin
from .import models

@admin.register(models.SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('nom',)


@admin.register(models.SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','message',)

@admin.register(models.Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('auteur','metier',)

@admin.register(models.UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(models.Newlatters)
class NewlattersAdmin(admin.ModelAdmin):
    list_display = ('email',)


