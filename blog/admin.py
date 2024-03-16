from django.contrib import admin
from django.db import models
from .models import Tag, Category, BlogPost
from froala_editor.widgets import FroalaEditor
from django.utils.html import mark_safe

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'display_post_image')
    list_filter = ("publish_date",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def display_post_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; border-radius: 50%;">')
        else:
            return 'No Image'
    display_post_image.short_description = 'Post Image'



    formfield_overrides = {
        models.TextField: {'widget': FroalaEditor(options={'toolbarInline': False, 'height': 400, 'theme': 'dark'})},
    }

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
