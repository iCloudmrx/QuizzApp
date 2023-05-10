from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Test(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    max_attemps = models.PositiveIntegerField()
    pass_percentage = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(now()+timedelta(days=7))
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


@receiver(pre_save, sender=CheckQuestion)
def check_answer(sender, instance, *args, **kwargs):
    if instance.given_answer == instance.true_answer:
        instance.true_answer = True


@receiver(pre_save, sender=CheckTest)
def check_test(sender, instance, *args, **kwargs):
    checktest = instance
    checktest.finded_question = CheckQuestion.objects.filter(
        check_test=checktest, is_true=True).count()
    try:
        checktest.percentage = (
            checktest.finded_question / checktest.test.question_set.count()) * 100
        if checktest.test.pass_percentage <= checktest.percentage:
            checktest.user_passed = True
    except:
        pass
