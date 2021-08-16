from django.db import models

# Create your models here.
class Feedback(models.Model):
    Uname = models.CharField(max_length=50)
    feedback = models.TextField()
    def __str__(self):
        return "Message from " + self.Uname

class Post(models.Model):
    heading = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return "Post : " + self.heading