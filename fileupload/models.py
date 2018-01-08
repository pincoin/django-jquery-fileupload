from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=255,
        help_text="The page title as you'd like it to be seen by the public",
    )

    body = models.TextField(
        verbose_name='content body',
    )

    slug = models.SlugField(
        verbose_name='slug',
        help_text='A short label containing only letters, numbers, underscores or hyphens for URL',
        max_length=255,
        unique=True,
        allow_unicode=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fileupload:post-detail', args=[self.slug, ])


class Attachment(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='file name',
        help_text="Defaults to filename, if left blank",
    )

    file = models.ImageField(
        verbose_name='uploaded file',
        upload_to="attachment",
    )

    post = models.ForeignKey(
        'fileupload.Post',
        verbose_name='post',
        related_name='attachments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        verbose_name='created time',
        auto_now_add=True,
    )

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return reverse('fileupload:attachment-detail', args=[self.slug, ])
