from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    num_stars = models.IntegerField(default=2)
    mfg_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    def show_desc(self):
        return self.description[:50]