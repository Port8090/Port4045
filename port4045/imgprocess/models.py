from django.db import models

# Create your models here.
class MyModel(models.Model):
    my_file = models.FileField(upload_to='uploads/')

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title