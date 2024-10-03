from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import the Django default User model

# ! Declaring Model for Category
class Category(models.Model):
    # ? Model Fields
    name = models.CharField(max_length=100, unique=True)  # Name of the category, unique constraint to avoid duplicates

    def __str__(self):
        return self.name


# ! Declaring Task Model
class Task(models.Model):
    # Choices declarations
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    # ? Model Fields
    title = models.CharField(max_length=150)  # Title: String, required
    description = models.TextField(default="No description provided", null=False)  # Non-null description with default
    due_date = models.DateField()  # Due date: Date, required
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default=LOW)  # Priority field with default 'Low'
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)  # Status field with default 'Pending'
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Allow tasks without categories
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link task to User, delete tasks if user is deleted
    completed_at = models.DateTimeField(null=True, blank=True)  # Completed at: DateTime, can be null/blank

    # Mark the task as completed and set the completed_at timestamp
    def mark_complete(self):
        self.completed_at = timezone.now()  # Use Django's timezone.now()
        self.status = self.COMPLETED
        self.save()

    # Define a string representation for easier identification of objects
    def __str__(self):
        return self.title
