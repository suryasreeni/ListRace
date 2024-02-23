from django.db import models

class place(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class review(models.Model):
    image=models.ImageField(upload_to='pics')
    place=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    review=models.TextField()
    def __str__(self):
        return self.name

