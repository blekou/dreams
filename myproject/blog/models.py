from django.db import models


class Article(models.Model):

    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Article')
    date = models.DateTimeField(auto_now_add=False)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre



class Auteur(models.Model):
    
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/Article')
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='article_auteur')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'

    def __str__(self):
        return self.nom


class Commentaire(models.Model):
    
    nom = models.CharField(max_length=200)
    message = models.TextField()
    photo = models.ImageField(upload_to='images/Commentaire')
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='article_commentaire')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.nom


class Likes(models.Model):
    
    auteur = models.CharField(max_length=200)
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='article_likes')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Likes'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return self.auteur


class Categorie(models.Model):
    
    nom = models.CharField(max_length=200)
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='article_categorie')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom









