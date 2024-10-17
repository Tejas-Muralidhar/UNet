from django.db import models
from ngos.models import NGO

# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = [
        ('complete', 'Complete'),
        ('ongoing', 'Ongoing'),
        ('future_event', 'Future Event'),
        ('cancelled', 'Cancelled'),
        # Add more status choices as needed
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()  # Changed 'desc' to 'description' for clarity
    start_date = models.DateField()  # For storing the start date
    end_date = models.DateField()  # For storing the end date
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # Choice field
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)  # Foreign key to NGO model

    def __str__(self):
        return self.title
