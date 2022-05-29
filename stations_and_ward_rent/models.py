from django.db import models

# Create your models here.
from poultry_products.models import Region, Governorate
class StationAndWard(models.Model):

    image_file = models.ImageField(
        upload_to="products/%Y/%m/%d",
        blank=True,
        null=True,
    )
    TYPE = (
        ("FOR_RENT", "FOR_RENT"),
        ("FOR_SALE", "FOR_SALE"),
    )
    rent_or_sale= models.CharField(max_length=20, choices=TYPE, default="FOR_RENT")

    product_name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)

    
    total_space = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    location = models.TextField(blank=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.product_name
