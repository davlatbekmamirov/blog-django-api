# Generated by Django 4.2.1 on 2023-05-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='username'),
        ),
    ]
