# Generated by Django 3.1.3 on 2021-04-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fulllname', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
