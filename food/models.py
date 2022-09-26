from distutils.command.upload import upload
from django.db import models

from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    image = models.ImageField(upload_to='image_cat/', blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Food(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    description = RichTextField(verbose_name='Text')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Date_create')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL')
    category = models.ForeignKey(
        Category, 
        related_name='food',
        verbose_name='category',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
        )
    tag = models.ManyToManyField(Tag, verbose_name='Tags')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("food_single", kwargs={"slug": self.slug})
    
    
    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

class Comment(models.Model):
    name = models.CharField(verbose_name='Name', max_length=150)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    photo = models.ImageField(verbose_name='Photo', upload_to='image/', blank=True, null=True)
    message = models.TextField(max_length=500, verbose_name='Text')
    post = models.ForeignKey(Food, related_name='comment', verbose_name='Comment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'