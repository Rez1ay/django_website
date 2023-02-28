from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address')
    search_fields = ('id', 'user', 'address')
    list_display_links = ('id', 'user', 'address')


admin.site.register(Profile, ProfileAdmin)
