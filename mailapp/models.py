from django.db import models

# Create your models here.
 
class MailBox(models.Model):
    name = models.CharField(max_length = 150)
    email_id = models.EmailField(max_length=150)
    subject = models.CharField(max_length = 150)
    message = models.TextField()
