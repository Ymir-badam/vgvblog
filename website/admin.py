from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "is_published", "published_at")
    list_filter = ("category", "is_published")
    search_fields = ("title", "content", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    fieldsets = (
        (None, {"fields": ("title", "slug", "category", "author")}),
        ("Content", {"fields": ("excerpt", "content", "cover_image")}),
        ("Publishing", {"fields": ("is_published", "published_at")}),
    )
