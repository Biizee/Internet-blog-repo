from django.db import models

# Create your models here.
    
class Comments(models.Model):
    text = models.TextField()
    autor = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    date_with_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    date_with_time = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey(Comments, on_delete=models.PROTECT)

    def __str__(self):
        return self.name