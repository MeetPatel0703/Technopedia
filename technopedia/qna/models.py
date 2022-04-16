from django.db import models
from account.models import TechUser
from generic.models import BaseField


class Question(BaseField):
    user = models.ForeignKey(TechUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, null=True)

    PENDING = 0
    SOLVED = 1
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (SOLVED, 'Solved'),
    )
    status = models.IntegerField(
        default=PENDING, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "questions"


class Answer(BaseField):
    user = models.ForeignKey(TechUser, on_delete=models.CASCADE)
    queid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2000)
    # likecount = models.IntegerField(default=0)
    likecount = models.ManyToManyField(
        TechUser, related_name='likes', blank=True)
    # dislikecount = models.IntegerField(default=0)
    dislikecount = models.ManyToManyField(
        TechUser, related_name='dislikes', blank=True)

    PENDING = 0
    CORRECT = 1
    RIGHT_CHOICES = (
        (PENDING, 'Pending'),
        (CORRECT, 'Correct'),
    )
    markAsSolution = models.IntegerField(
        default=PENDING, choices=RIGHT_CHOICES)

    # def total_like(self):
    #     return self.likecount.all.count()

    class Meta:
        db_table = "answers"
