from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # def __str__(self):
    #     return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# class Food(models.Model):
#     name = models.CharField(max_length=400)
#     description = models.CharField(_("details"), max_length=200)
#     rate = models.CharField(_("rank"), max_length=200)
#     pun_date = models.DateField(_("pulication_time"))
#     price = models.IntegerField
#     time = models.IntegerField(_("time to ready"))
#     photo = models.ImageFiled(upload_to ='mysite/')
         


        