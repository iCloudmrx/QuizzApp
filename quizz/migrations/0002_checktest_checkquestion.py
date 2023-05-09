# Generated by Django 4.0.5 on 2023-05-09 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finded_question', models.PositiveIntegerField(default=0)),
                ('user_passed', models.BooleanField(default=False)),
                ('percentage', models.PositiveBigIntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.test')),
            ],
        ),
        migrations.CreateModel(
            name='CheckQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_answer', models.CharField(help_text='E.x: a', max_length=1)),
                ('true_answer', models.CharField(help_text='E.x: a', max_length=1)),
                ('is_true', models.BooleanField(default=False)),
                ('check_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.checktest')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.question')),
            ],
        ),
    ]
