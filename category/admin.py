from django.contrib import admin
from .models import Category

class CatergoyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
# Register your models here.
admin.site.register(Category)