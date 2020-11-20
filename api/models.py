from django.db import models

class Lead(models.Model):
    location_choices = [
        ['Country', 'Country'],
        ['City', 'City'],
        ['Zip', 'Zip']
    ]
    status_choices = [
        ['Created', 'Created'],
        ['Contacted', 'Contacted']
    ]
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    mobile = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    location_type = models.CharField(choices=location_choices, max_length=10)
    location_string = models.TextField()
    status = models.CharField(choices=status_choices, max_length=10)
    communication = models.TextField(null=True)