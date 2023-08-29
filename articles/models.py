from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)