from django.contrib import admin
from blogging.models import Post, Category
# Register your models here.


class CategoryInLine(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
               ]

    class Meta:
        model = Category

    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
