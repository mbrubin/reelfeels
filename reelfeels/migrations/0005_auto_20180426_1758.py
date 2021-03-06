# Generated by Django 2.0.2 on 2018-04-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reelfeels', '0004_auto_20180426_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewinstance',
            name='previous_anger',
            field=models.IntegerField(default=0, verbose_name='Previous Anger'),
        ),
        migrations.AlterField(
            model_name='viewinstance',
            name='previous_disgust',
            field=models.IntegerField(default=0, verbose_name='Previous Disgust'),
        ),
        migrations.AlterField(
            model_name='viewinstance',
            name='previous_happiness',
            field=models.IntegerField(default=0, verbose_name='Previous Happiness'),
        ),
        migrations.AlterField(
            model_name='viewinstance',
            name='previous_sadness',
            field=models.IntegerField(default=0, verbose_name='Previous Sadness'),
        ),
        migrations.AlterField(
            model_name='viewinstance',
            name='previous_surprise',
            field=models.IntegerField(default=0, verbose_name='Previous Surprise'),
        ),
    ]
