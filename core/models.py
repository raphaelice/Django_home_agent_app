from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=250)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to='/images')
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
