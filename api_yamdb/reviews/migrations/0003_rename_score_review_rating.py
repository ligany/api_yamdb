# Generated by Django 3.2 on 2023-05-01 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230427_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='score',
            new_name='rating',
        ),
    ]
