from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    profile_photo = models.ImageField(null=True)

    def __str__(self):
        return self.username
    
class Entry(models.Model):
    name = models.CharField(max_length=100)
    writeup = models.TextField()
    photo_album = models.ImageField()
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE, related_name='entries')

    def __str__(self):
        return self.name
    
class Journal(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journals')
    def __str__(self):
        return self.title