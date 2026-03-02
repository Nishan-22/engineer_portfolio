from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published_at', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    list_editable = ('status',)

    def save_model(self, request, obj, form, change):
        if obj.status == 'published' and not obj.published_at:
            from django.utils import timezone
            obj.published_at = timezone.now()
        super().save_model(request, obj, form, change)
