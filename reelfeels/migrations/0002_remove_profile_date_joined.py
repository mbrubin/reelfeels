# Generated by Django 2.0.2 on 2018-04-08 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reelfeels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_joined',
        ),
    ]
