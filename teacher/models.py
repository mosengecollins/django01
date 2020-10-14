from django.db import models

# Create your models here.

from django.urls import reverse

class Teacher(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    description = models.TextField()
    birth_date = models.DateTimeField('birth date ')
    entry_date = models.DateTimeField('entry date ')
    photo = models.CharField(max_length=20)
    idBirthCertificate = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    def get_absolute_url(self):
        return reverse('teacher-detail', kwargs={'pk': self.pk})



class TelTeacher(models.Model):
    telTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    telNrTeacher = models.CharField(max_length=30)

    def __str__(self):
        return self.telNrTeacher
