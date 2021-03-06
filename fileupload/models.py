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

    created = models.DateTimeField(
        verbose_name='created time',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk, ])


class AbstractAttachment(models.Model):
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

    created = models.DateTimeField(
        verbose_name='created time',
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class Attachment(AbstractAttachment):
    post = models.ForeignKey(
        'fileupload.Post',
        verbose_name='post',
        related_name='attachments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'attachment'
        verbose_name_plural = 'attachments'
        ordering = ['-created']

    def __str__(self):
        return self.name
