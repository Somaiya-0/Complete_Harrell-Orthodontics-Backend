from django.contrib import admin
from .models import NavCategory, Page, PageSection, DownloadableForm


class PageSectionInline(admin.TabularInline):
    model = PageSection
    extra = 1


class DownloadableFormInline(admin.TabularInline):
    model = DownloadableForm
    extra = 1


@admin.register(NavCategory)
class NavCategoryAdmin(admin.ModelAdmin):
    list_display = ("label", "order")
    ordering = ("order",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "nav_category", "is_published", "show_in_nav", "nav_order", "updated_at")
    list_filter = ("nav_category", "is_published", "show_in_nav")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PageSectionInline, DownloadableFormInline]
    search_fields = ("title", "short_description")
