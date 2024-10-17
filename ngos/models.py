from django.db import models

# Create your models here.


class NGO(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()  # Changed 'desc' to 'description' for clarity
    location = models.CharField(max_length=255)
    web_links = models.URLField(max_length=200, blank=True)  # Allowing blank for optional field
    email = models.EmailField(max_length=255, unique=True)  # Ensure email is unique
    phone = models.CharField(max_length=15, blank=True)  # Allowing blank for optional field
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on update
    profile_picture = models.ImageField(upload_to='ngo_profile_pictures/', blank=True, null=True)
    username = models.CharField(max_length=150, unique=True)  # Ensure username is unique
    password = models.CharField(max_length=128)  # Storing hashed password

    def __str__(self):
        return self.name