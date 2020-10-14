from django.db import models

# Create your models here.

from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    where = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})
