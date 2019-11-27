from django.db import models

class UserBook(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    link = models.URLField()

    author = models.CharField(max_length=200)
    og_price = models.CharField(max_length=200)

    publisher = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)

    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title