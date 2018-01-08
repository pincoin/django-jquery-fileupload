from django.contrib import admin

from .models import Attachment


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'post', 'created')


admin.site.register(Attachment, AttachmentAdmin)
