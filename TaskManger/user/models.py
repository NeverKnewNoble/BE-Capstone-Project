from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key with auto-incremented ID
    username = models.CharField(max_length=150, unique=True)  # Username field, max length 150, must be unique
    email = models.EmailField(unique=True)  # Email field, must be unique
    password = models.CharField(max_length=128)  # Password field with a max length of 128

    # Add this line to define REQUIRED_FIELDS for Django
    REQUIRED_FIELDS = ['email']  # Specify that email is required for user creation

    def __str__(self):
        return self.username  # Return the username for easy identification
