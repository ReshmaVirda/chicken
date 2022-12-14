from django.db import models
from user_profile.models import User
from poultry_products.models import Governorate
from feed.models import ImageFile
class ProductEquipment(models.Model):

    image_file = models.OneToOneField(
        ImageFile,
        on_delete=models.CASCADE,
        null=True,
    )


    product_name = models.CharField(max_length=200, db_index=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE,blank=True,null=True)
    region = models.TextField(blank=True,null=True)
    location = models.TextField(blank=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.product_name
    @property
    def get_image_url(self):
        if self.image_file:
            if self.image_file.image_url:
                return self.image_file.image_url
