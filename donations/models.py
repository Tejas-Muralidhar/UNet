from django.db import models

# Create your models here.
from users.models import User
from ngos.models import NGO # Import the User and Ngo models

class Donation(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)  # Foreign key to Ngo
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User

    def __str__(self):
        return f"{self.amount} donated to {self.ngo.name} by {self.user.username} on {self.date}"
