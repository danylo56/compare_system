from django.db import models


class Girl(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.name + ' ' + str(self.rating)

    def do_update(self):
        self.rating += 1

    def do_downgarde(self):
        self.rating -= 1
# Create your models here.
