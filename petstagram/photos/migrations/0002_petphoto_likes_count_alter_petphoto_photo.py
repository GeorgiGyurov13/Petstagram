# Generated by Django 5.0.4 on 2024-04-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='pet_photos/'),
        ),
    ]