from django.db import models

# Create your models here.
class ImageFile(models.Model):
    """
    add this class and the following fields
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("-created_at",)

    file_url = models.FileField(
        upload_to="products/%Y/%m/%d",
        blank=True,
        null=True,
    )
    def _str_(self):
        return self.file_url

    @property
    def image_url(self):
        if self.file_url and hasattr(self.file_url, 'url'):
            return self.file_url.url
        else:
            return None