# Generated by Django 2.0.7 on 2020-11-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0002_auto_20201123_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
