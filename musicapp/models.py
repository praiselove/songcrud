from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model):
   first_name = models.CharField(max_length=400)
   last_name = models.CharField(max_length=400)
   age = models.IntegerField()

   def __str__(self):
      return self.first_name + " " + self.last_name + " " + self.age


class Song(models.Model):
   artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
   title = models.CharField(max_length=400)
   date_released = models.DateField()
   likes = models.CharField(max_length=400)
   # artiste_id = models.CharField(max_length=400)

   def __str__(self):
      return self.artiste.first_name + " " + self.artiste.last_name + " " + self.artiste.age + " " + self.artiste.title + " " + self.artiste.date_released + " " + self.artiste.likes + " " + self.artiste.artiste_id
      
class Lyric(models.Model):
   artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
   content = models.CharField(max_length=400)
   song_id = models.CharField(max_length=400)

   def __str__(self):
      return self.artiste.first_name + " " + self.artiste.last_name + " " + self.artiste.age + " " + self.artiste.title + " " + self.artiste.date_released + " " + self.artiste.likes + " " + self.artiste.artiste_id + " " + self.artiste.content + " " + self.artiste.song_id