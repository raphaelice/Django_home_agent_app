from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class House(models.Model):

    TYPE = (
        ('SC', 'Self-contain'),
        ('1RA', 'One room apartment'),
        ('2RA', 'Two room apartment'),
        ('3RA', 'Three room apartment'),
        ('4RA', 'Four room apartment')
    )

    name = models.CharField(max_length=250)
    type = models.CharField(max_length=3, choices=TYPE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to='core/static/core/images')
    price = models.IntegerField()
    water = models.BooleanField(default=False)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.name
