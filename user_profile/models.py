from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    add this class and the following fields

    """
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    fcm_token = models.CharField(max_length=100, null=True, blank=True)
    profie_photo_url = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    otp = models.IntegerField(default=1234)
    is_registred = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)

    def _str_(self):
        return self.user

    @property
    def image_url(self):
        if self.profie_photo_url and hasattr(self.profie_photo_url, "url"):
            return self.profie_photo_url.url
        else:
            return None
