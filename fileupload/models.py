from django.db import models
from django.utils.text import slugify


class Attachment(models.Model):
    file = models.ImageField(upload_to="attachment")
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.file.name, allow_unicode=True)

        super(Attachment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # remove a file from storage
        self.file.delete(False)

        super(Attachment, self).delete(*args, **kwargs)
