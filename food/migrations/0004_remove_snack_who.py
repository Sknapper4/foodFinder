# Generated by Django 2.1.7 on 2019-03-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20190320_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snack',
            name='who',
        ),
    ]
