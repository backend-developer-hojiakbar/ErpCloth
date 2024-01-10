from django.db import models

class Category(models.Model):
    nomi = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomi

class Product(models.Model):
    nomi = models.CharField(max_length=120)
    code = models.IntegerField()
    kategoriya = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/")
    kelganNarxi = models.IntegerField()
    sotishNarxi = models.IntegerField()
    minumSotishNarx = models.IntegerField()
    soni = models.IntegerField()
    haqida = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomi


class Order(models.Model):
    maxsulotId = models.ForeignKey(Product, on_delete=models.CASCADE)
    sotilganNarx = models.IntegerField()
    soni = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.maxsulotId)

