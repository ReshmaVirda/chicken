from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    add this class and the following fields

    """

    ROLES = (
        ("BREEDER", "BREEDER"),
        ("MERCHANT", "MERCHANT"),
        ("OTHER", "OTHER"),

    )
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    fcm_token = models.CharField(max_length=100, null=True, blank=True)
    profile_photo_url = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    otp = models.IntegerField(default=1234)
    is_registred = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLES, default="BREEDER")

    class Meta:
        ordering = ("-created_at",)

    def _str_(self):
        return self.user

    @property
    def image_url(self):
        if self.profile_photo_url and hasattr(self.profile_photo_url, "url"):
            return self.profile_photo_url.url
        else:
            return None
