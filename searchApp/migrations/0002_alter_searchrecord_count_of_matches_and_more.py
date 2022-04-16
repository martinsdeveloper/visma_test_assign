# Generated by Django 4.0.3 on 2022-04-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchrecord',
            name='count_of_matches',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='searchrecord',
            name='keywords',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='searchrecord',
            name='url',
            field=models.URLField(),
        ),
    ]
