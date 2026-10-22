from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    durations = models.SmallIntegerField(default=4)

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, default="+998991234567")
    birth_year = models.SmallIntegerField(default=2010)
    image = models.ImageField(upload_to="images/students/", null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
