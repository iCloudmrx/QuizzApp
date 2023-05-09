from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self


class Test(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    max_attemps = models.PositiveIntegerField()
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['-start_date'])
        ]

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)
    true_answer = models.CharField(max_length=255, help_text="E.x: a")

    def __str__(self):
        return self.question


class CheckTest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    finded_question = models.PositiveIntegerField(default=0)
    user_passed = models.BooleanField(default=False)
    percentage = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.student.username


class CheckQuestion(models.Model):
    check_test = models.ForeignKey(CheckTest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    given_answer = models.CharField(max_length=1, help_text="E.x: a")
    true_answer = models.CharField(max_length=1, help_text="E.x: a")
    is_true = models.BooleanField(default=False)
