from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True,blank=False,null=False)
    desc=models.TextField(blank=True)
    pict=models.ImageField(upload_to='category',blank=False,null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    class Meta:
        ordering=['name','desc','user']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return '{}'.format([self.name])

class Movie(models.Model):
    name = models.CharField(max_length=250, unique=True,blank=False,null=False)
    desc = models.TextField(blank=True)
    actors = models.TextField(blank=True)
    utubelink = models.TextField(blank=True)
    pict = models.ImageField(upload_to='movieposter',blank=False,null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)
    released = models.DateField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    class Meta:
        ordering = ['name','updated','user']
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
    def __str__(self):
        return '{}'.format(self.name)

class Rating(models.Model):
    name=models.ForeignKey(Movie,on_delete=models.CASCADE,blank=True)
    review=models.TextField(max_length=500,blank=True,null=True)
    rating=models.IntegerField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    class Meta:
        ordering=['name','rating','user']
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
    def __str__(self):
        return '{}'.format([self.name])
class Favorites(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    class Meta:
        ordering=['movie','user']
        verbose_name = 'Favorites'
        verbose_name_plural = 'Favorites'
    def __str__(self):
        return '{}'.format([self.movie])