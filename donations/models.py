from django.db import models
from django.utils.timezone import now
from ngos.models import NGO
from users.models import User


class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    ngo_id = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='donations')
    date = models.DateTimeField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Donation #{self.id} - {self.amount} by User {self.user_id_id} to NGO {self.ngo_id_id}"
