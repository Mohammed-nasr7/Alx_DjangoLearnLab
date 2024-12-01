from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Previous Book model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change an existing book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title

# Previous Library model
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# New UserProfile model for role-based access control
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()