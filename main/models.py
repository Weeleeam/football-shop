import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('shirts', 'Shirts'),
        ('gloves', 'Gloves'),
        ('balls', 'Balls'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    product_views = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()