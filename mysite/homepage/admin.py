from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'candle_count')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'caption', 'user__username')
    readonly_fields = ('created_at', 'candle_count')
    fieldsets = (
        ('Pet Information', {
            'fields': ('user', 'title', 'caption', 'image')
        }),
        ('Metadata', {
            'fields': ('candle_count', 'created_at')
        }),
    )
