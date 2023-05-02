# Generated by Django 3.2 on 2023-05-06 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20230506_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'User with that username already exists.'}, help_text='Required. 150 characters or fewer.Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[\\\\w.@+-]+\\\\z')], verbose_name='Никнейм'),
        ),
    ]