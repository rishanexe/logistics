# Generated by Django 2.1.7 on 2019-03-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logsapp', '0002_details_orderdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name_plural': 'Details'},
        ),
    ]