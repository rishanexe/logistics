# Generated by Django 2.1.7 on 2019-03-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsapp', '0008_auto_20190331_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='good_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]