# Generated by Django 2.2 on 2020-03-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='girl',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='girl',
            name='photo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
