from django.db import models

# Create your models here.
class UserIN(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  age=models.IntegerField()
  image=models.ImageField(upload_to='img/', blank=True, null=True)
  
  
  def __str__(self):
    return self.name