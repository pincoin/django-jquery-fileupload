from django.contrib import admin

from .models import (
    Attachment, Post
)


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'post', 'created')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Post, PostAdmin)
