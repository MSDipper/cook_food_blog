# Generated by Django 4.1.1 on 2022-09-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name')),
                ('content_us', models.TextField(verbose_name='About us')),
                ('mini_content', models.CharField(max_length=50, verbose_name='Content')),
                ('main_image', models.ImageField(upload_to='image_about/', verbose_name='Main image')),
                ('left_image', models.ImageField(upload_to='image_about/', verbose_name='Left image')),
                ('video_us', models.FileField(upload_to='video/', verbose_name='Video')),
                ('slug', models.SlugField(max_length=100, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'About us',
                'verbose_name_plural': 'About us',
            },
        ),
    ]
