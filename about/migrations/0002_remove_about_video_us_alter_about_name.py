# Generated by Django 4.1.1 on 2022-09-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='video_us',
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
    ]