# Generated by Django 4.0.6 on 2022-12-27 14:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_alter_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
