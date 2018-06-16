from django.contrib import admin
from .models import Article, Tags, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'status', 'views', 'author')
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags)
admin.site.register(Category)
