from django.db import models
from django.shortcuts import reverse

class Location(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name



class House(models.Model):

    STYLE = (
        ('SC', 'Self-contain'),
        ('1RA', 'One room apartment'),
        ('2RA', 'Two room apartment'),
        ('3RA', 'Three room apartment'),
        ('4RA', 'Four room apartment')
    )

    name = models.CharField(max_length=250)
    style = models.CharField(max_length=3, choices=STYLE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    first_price = models.PositiveIntegerField()
    subsequent_price = models.PositiveIntegerField()
    water = models.BooleanField(default=False)
    vacant = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=(self.pk,))
        
class Image(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='house-images')

    def __str__(self):
        return f"{self.house.name} images"