# Generated by Django 2.1.7 on 2019-03-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsapp', '0005_auto_20190319_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='details',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='mobile',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
