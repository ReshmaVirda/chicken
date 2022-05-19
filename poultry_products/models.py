from django.db import models


class ProductName(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Governorate(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(models.Model):

    image_file = models.ImageField(
        upload_to="products/%Y/%m/%d",
        blank=True,
        null=True,
    )
    product_name = models.ForeignKey(
        ProductName, related_name="products", on_delete=models.CASCADE
    )
    other_product = models.CharField(max_length=200, db_index=True)

    description = models.TextField(blank=True)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average_weight = models.CharField(max_length=200, db_index=True)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.TextField(blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.other_product
