from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name + self.surname

    class Meta:
        abstract = True


class Teacher(User):
    reputation = models.IntegerField()


class Student(User):
    score = models.IntegerField()

