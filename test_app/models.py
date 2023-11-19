from django.db import models


class Post(models.Model):
    img_code = models.TextField()
    description = models.CharField(max_length=120)
    