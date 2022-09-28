from tabnanny import verbose
from django.db import models




class About(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null=True)
    content_us = models.TextField(verbose_name='About us')
    mini_content = models.CharField(max_length=50, verbose_name='Content')
    main_image = models.ImageField(verbose_name='Main image', upload_to='image_about/')
    left_image = models.ImageField(verbose_name='Left image', upload_to='image_about/')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    
    def __str__(self):
        return f'{self.mini_content}'
    
    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'
    