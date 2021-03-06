from datetime import datetime
from django.db import models


# Create your models here.

class Course(models.Model):
    """Represents a course in the class schedule."""
    id = models.CharField(primary_key=True, max_length=100)
    course_date = models.DateField(default=datetime.utcfromtimestamp(0))
    course_id = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    section = models.TextField()
    credits = models.FloatField()
    capacity = models.IntegerField()
    enrolled = models.IntegerField()
    start_end = models.TextField()
    location = models.TextField()

class Days(models.Model):
    """Represents the separate days which a class is held on for a course."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=5)

class Instructors(models.Model):
    """Represents the separate instructors which teach a class."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.CharField(max_length=256)

class Conditions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    condition = models.CharField(max_length=16)

class Prerequisites(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    prerequisite = models.CharField(max_length=256)

class Requirements(models.Model):
    """Represents the requirements which are fulfilled by this course."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=256, null=True)
