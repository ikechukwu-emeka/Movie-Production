# Generated by Django 4.1.1 on 2022-10-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='passport',
            field=models.ImageField(upload_to='images/audition'),
        ),
    ]