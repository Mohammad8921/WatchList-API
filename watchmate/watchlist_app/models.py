from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey('StreamPlatform', on_delete=models.CASCADE, null=True, related_name='watchlist')
    created = models.DateTimeField(auto_now_add=True)
    ave_rating = models.FloatField(default=0)
    rating_number = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=300)
    movie = models.ForeignKey('WatchList', on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Review " + str(self.id)
         
    
    