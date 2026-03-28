from django.db import models
import random
import string

def generate_reference():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class Report(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('disputed', 'Disputed'),
        ('closed', 'Closed'),
    ]

    reference_number = models.CharField(max_length=8, default=generate_reference, editable=False, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    fault_type = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='fault_photos/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reference_number} - {self.fault_type} - {self.status}"



