from django.contrib import admin
from .import models

@admin.register(models.Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('nom','article',)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre',)


@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom','message',)

@admin.register(models.Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('auteur',)

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','article',)

