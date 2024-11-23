from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES_1 = [
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Food', 'Food'),
    ]

    CATEGORY_CHOICES_2 = [
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
        ('Service', 'Service'),
    ]

    appname = models.CharField(max_length=100)
    applink = models.URLField(max_length=200)
    category1 = models.CharField(max_length=50, choices=CATEGORY_CHOICES_1)
    category2 = models.CharField(max_length=50, choices=CATEGORY_CHOICES_2)
    add_points = models.IntegerField()
    logo = models.ImageField(upload_to='images/')  # Store logo image


    def __str__(self):
        return self.appname
