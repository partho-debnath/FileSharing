# Generated by Django 4.1 on 2022-08-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0002_file_userip'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userip', models.GenericIPAddressField()),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='userip',
        ),
    ]
