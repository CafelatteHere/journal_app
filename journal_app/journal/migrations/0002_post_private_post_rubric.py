# Generated by Django 4.0.6 on 2022-12-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='rubric',
            field=models.CharField(choices=[('No rubric', 'No rubric'), ('Daily life', 'Daily life'), ('Travel', 'Travel'), ('Sport', 'Sport'), ('News', 'News'), ('Food', 'Food'), ('Discussion', 'Discussion'), ('Other', 'Other')], default='No rubric', max_length=100),
        ),
    ]
