from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
    file = models.ImageField(
        verbose_name='uploaded file',
        upload_to="attachment",
    )

    slug = models.SlugField(
        verbose_name='slug',
        help_text='A short label containing only letters, numbers, underscores or hyphens for URL',
        max_length=255,
        unique=True,
        allow_unicode=True,
    )

    post = models.ForeignKey(
        'fileupload.Post',
        verbose_name='post',
        related_name='attachments',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return reverse('fileupload:attachment-detail', args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.file.name, allow_unicode=True)

        super(Attachment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # remove a file from storage
        self.file.delete(False)

        super(Attachment, self).delete(*args, **kwargs)
