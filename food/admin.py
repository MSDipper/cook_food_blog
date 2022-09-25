from django.contrib import admin

from foods.models import Category, Tag, Food, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    save_on_top = True
    save_as = True
    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass