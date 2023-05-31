from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class user(models.Model):
    User_id = models.IntegerField(primary_key=True)
    User_name = models.TextField()
    User_password = models.TextField()
    Is_admin = models.IntegerField()
    Is_login = models.IntegerField(default=0)
    def __str__(self):
        return f"User ID: {self.User_id}, User Nicename: {self.User_name}"
    
    def get_absolute_url(self):
        return reverse_lazy('user.info', kwargs={'pk': self.pk})