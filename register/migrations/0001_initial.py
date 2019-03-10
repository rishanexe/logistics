# Generated by Django 2.1.7 on 2019-03-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=16)),
                ('usertype', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Login',
            },
        ),
    ]
