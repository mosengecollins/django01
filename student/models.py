from django.db import models

# Create your models here.


# Create your models here.

#from django.db import models

# Create your models here.

#from django.db import models


class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    description = models.TextField()
    birth_date = models.DateTimeField('birth date ')
    entry_date = models.DateTimeField('entry date ')
    photo = models.CharField(max_length=20)
    idBirthCertificate = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Tel(models.Model):
    tel = models.ForeignKey(Student, on_delete=models.CASCADE)
    telNr = models.CharField(max_length=30)

    def __str__(self):
        return self.telNr
