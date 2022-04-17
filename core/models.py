from django.db import models

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
    pictures = models.ImageField(upload_to='core/static/core/images/')
    price = models.PositiveIntegerField()
    water = models.BooleanField(default=False)
    occupied = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

