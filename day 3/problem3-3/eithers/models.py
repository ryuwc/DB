from email.policy import default
from random import choices
from secrets import choice
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)

flag_chocies = (
    (1, 'Red'),
    (0, 'Blue')
)
class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField(choices=flag_chocies, default='RED')
    content = models.CharField(max_length=100)


