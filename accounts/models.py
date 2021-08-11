from django.db import models

# Create your models here.
class Feedback(models.Model):
    Uname = models.CharField(max_length=50)
    feedback = models.TextField(max_length=300)

    
    
    def __str__(self):
        return "Message from " + self.Uname

class Post(models.Model):
    heading = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    def __str__(self):
        return "Post : " + self.heading