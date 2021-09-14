from django.contrib import admin
from blogging.models import Post, Category, CategoryInLine
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
               ]
    exclude = ('posts',)


admin.site.register(Post)
admin.site.register(Category)
