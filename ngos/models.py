from django.db import models


class NGO(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    purpose = models.TextField()

    def __str__(self):
        return self.name
