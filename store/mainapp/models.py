from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name='name product', max_length=128)
    desc = models.TextField(verbose_name='description product')
    price = models.DecimalField(verbose_name='price', max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to="products_images", blank=True, default='no-image.jpg')
    quantity = models.PositiveIntegerField(verbose_name='quantity product', default=0)
    created_at = models.DateTimeField(verbose_name='add date product', auto_now_add=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

