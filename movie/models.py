from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from celebrity.models import Celebrity 


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, blank=False)    
    release_year = models.DateField(auto_now_add = True)
    duration = models.FloatField()
    language = models.CharField(max_length=50)
    link = models.URLField()
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )    
    description = models.TextField()
    image = models.ImageField(upload_to='movie', blank=True, null=True)
    actors = models.ManyToManyField(Celebrity)
    views = models.IntegerField(default=0)
    
    
def __str__(self):
        return self.title