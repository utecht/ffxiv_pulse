from django.contrib import admin
from content.models import *

# Register your models here.
@admin.register(Image, Editor, News, Feature, Guide)
class DefaultAdmin(admin.ModelAdmin):
    pass
