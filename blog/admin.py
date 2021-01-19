from django.contrib import admin
from .models import Category,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','published','author','concat_categories','created')
    ordering = ('created','author')
    search_fields = ('title','author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__title')

    def concat_categories(self,obj):
        return ", ".join([c.title for c in obj.categories.all().order_by('title')])

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
