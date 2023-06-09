# Generated by Django 4.2.1 on 2023-05-08 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('max_attemps', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.category')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('a', models.CharField(max_length=255)),
                ('b', models.CharField(max_length=255)),
                ('c', models.CharField(max_length=255)),
                ('d', models.CharField(max_length=255)),
                ('true_answer', models.CharField(help_text='E.x: a', max_length=255)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.test')),
            ],
        ),
        migrations.AddIndex(
            model_name='test',
            index=models.Index(fields=['-start_date'], name='quizz_test_start_d_21707b_idx'),
        ),
    ]
