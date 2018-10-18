from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=250,
        unique=True
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128
    )

    image = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT,
    )

    snippet = models.TextField(
        verbose_name='описание',
        blank=True
    )

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )



    def __str__(self):
        return self.name
