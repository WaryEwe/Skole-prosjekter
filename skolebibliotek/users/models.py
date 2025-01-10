from django.db import models
from django.contrib.auth.models import User
class UserModel(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.username
