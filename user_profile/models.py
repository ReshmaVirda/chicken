from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, mobile_no, first_name, last_name, address, location, country_code, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not mobile_no:
            raise ValueError('Users must have an mobile_no')

        user = self.model(
            mobile_no=mobile_no,
            first_name=first_name,
            last_name=last_name,
            address=address,
            location=location,
            country_code=country_code
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_no, first_name, last_name, address, location, country_code, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            mobile_no=mobile_no,
            first_name=first_name,
            last_name=last_name,
            address=address,
            location=location,
            country_code=country_code,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    mobile_no = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=5000, default="", blank=True, null=True)
    location = models.CharField(max_length=255, default="", blank=True, null=True)
    country_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'address', 'location', 'country_code']

    def __str__(self):
        return self.mobile_no

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

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
