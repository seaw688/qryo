# Generated by Django 2.0.7 on 2018-08-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yomarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcoupon',
            name='is_acitve',
            field=models.BooleanField(default=True),
        ),
    ]
