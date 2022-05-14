from django.db import models

from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image_file = models.ImageField(upload_to='products/%Y/%m/%d', blank=True,)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



    