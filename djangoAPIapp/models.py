from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=225)
    def __str__(self):
        return self.title

class Book (models.Model):
   title = models.CharField(max_length=150)
   Category = models.foreignkey(Category,related_name ='books',on_delete=models.CASCADDE)
   isbn = models.CharField(max_length=15)
   pages = models.CharField()
   price = models.CharField()
   stock = models.CharField()
   description = models.CharField()
   imageUrl = models.URLField()
   status =models.BooleanField(default= True)
   data_created =models.DateField(auto_now_add=True)

   class Meta:
      ordering = ['-date_created']
    
   def __str__(self):
        return self.title



class Product(models.Model):
    product_tage =models.CharField(max_length=10)
    name =models.CharField(max_length=100)
    Category = models.foreignkey(Category,related_name ='Product',on_delete=models.CASCADDE)
    price = models.CharField()   
    stock = models.CharField() 
    imageUrl = models.URLField()
    status =models.BooleanField(default= True)
    data_created =models.DateField(auto_now_add=True)

    class Meta:
      ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
