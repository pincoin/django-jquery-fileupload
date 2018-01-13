from django.contrib import admin

from .models import (
    Attachment, Post
)


class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 2


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'post', 'created')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    inlines = [AttachmentInline]


admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Post, PostAdmin)
