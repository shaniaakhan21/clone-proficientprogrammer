# Generated by Django 3.0.8 on 2020-07-24 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('birthdate', models.DateTimeField(default=datetime.datetime.now)),
                ('gender', models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE')], default='male', max_length=10)),
                ('pincode', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('gname', models.CharField(max_length=100)),
                ('gphone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=30)),
                ('ques', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default=False, max_length=10)),
            ],
        ),
    ]
