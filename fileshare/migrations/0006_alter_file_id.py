# Generated by Django 4.1 on 2022-08-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0005_remove_file_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
    ]
