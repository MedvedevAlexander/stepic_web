from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text
