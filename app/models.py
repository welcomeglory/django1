from django.db import models

class Contact(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField()
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.name

class Login(models.Model):
   username = models.CharField(max_length=100)
   password = models.CharField(max_length=100)

   def __str__(self):
      return self.username


class Member(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100, blank=True)
   phone = models.CharField(max_length=15, blank=True)
   address = models.CharField(max_length=255, blank=True)
   GENDER_CHOICES = [
      ('M', 'Male'),
      ('F', 'Female'),
      ('O', 'Other'),
   ]
   gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

   def __str__(self):
      return self.user.username


