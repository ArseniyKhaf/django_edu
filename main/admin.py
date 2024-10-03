from django.contrib import admin
from main.models import Category, Goods


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug"
    )

    list_display_links = (
        "name",
    )
    prepopulated_fields = {"slug": ("name",)}


class GoodsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    filter_vertical = (
        "category",
    )
    search_fields = (
        "name",
        "description",
    )
    list_filter = (
        "category",
        "adding_time",
    )
    empty_value_disply = "-пусто-"
    ordering = (
        "adding_time",
    )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
