# Generated by Django 3.1.2 on 2020-10-31 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20201101_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
