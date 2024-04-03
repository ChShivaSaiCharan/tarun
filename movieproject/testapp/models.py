from django.db import models

# Create your models here.
class MovieModel(models.Model):
    Release_Date=models.DateField()
    Movie_name=models.CharField(max_length=30)
    Hero_name=models.CharField(max_length=30)
    Heroine_name=models.CharField(max_length=30)
    rating=models.IntegerField()

    # & lt;
    # th & gt;
    # Release
    # Date & lt; / th & gt;
    # & lt;
    # th & gt;
    # Movie
    # Name & lt; / th & gt;
    # & lt;
    # th & gt;
    # Hero & lt; / th & gt;
    # & lt;
    # th & gt;
    # Heroine & lt; / th & gt;
    # & lt;
    # th & gt;
    # Rating & lt; / th & gt;
