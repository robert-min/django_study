from django.contrib import admin
from .models import *

# Register your models here.

# 방법 1 : register을 활용한 기법
# option class
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Category, CategoryAdmin)

# 방법 2 : anotation 기법
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "category", "price", "stock",
                    "available_display", "available_order", "created", "updated"]
    list_filter = ["available_display", "created", "updated", "category"]
    prepopulated_fields = {"slug": ("name", )}
    list_editable = ["price", "stock", "available_display", "available_order"]

