from django.db import models

# Create your models here.
class Quantity(models.Model):
    variant_name= models.CharField(max_length=100)

    def __str__(self):
        return self.variant_name
    

class GroceryItem(models.Model):
    product_id = models.AutoField
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    pub_date = models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="home/images", default="")
    quantity_type = models.ForeignKey(Quantity, blank=True, null=True, on_delete=models.PROTECT)

    
    class Meta:
        ordering=('title',)

    def __str__(self):
        return self.title



class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    
    def __str__(self):
        return self.name + 's order'
    

class Orderupdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)
    def __str__(self):
        return self.update_desc[0:7] + "..."
