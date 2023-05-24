from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Foo(models.Model):
    foo = models.IntegerField(default=0)

class Bar(models.Model):
    bar = models.IntegerField(default=0)
    fruit_salad = models.IntegerField(default=0)


