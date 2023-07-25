from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    img_url = models.TextField(null=True)

    def __str__(self):
        return self.username