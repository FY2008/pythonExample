from django.contrib import admin

from .models import User


class AuthorAdmin(admin.ModelAdmin):
    fields = ('username', 'nickname', 'avatar', 'email', 'qq', 'mobile',
              'password', 'is_superuser', 'last_login', 'date_joined',
              'web_site')

    list_display = ('username', 'avatar', 'email', 'nickname', 'qq', 'mobile',
                    'web_site')
    search_fields = ['username']


admin.site.register(User, AuthorAdmin)
