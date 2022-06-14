from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from shop.models import Product
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUser(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager

class Profile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emailVerified = models.BooleanField(default=False, null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)  
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='users/images', default='')

    def __str__(self):
        return str(self.id)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    orderId = models.CharField(max_length=100)
    cartItems = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(default=0)
    email = models.EmailField(default='')
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    pincode = models.IntegerField(default=480001, null=True, blank=True)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
@receiver(post_save, sender=MyUser)
def _post_save_receiver(sender, instance, created, *args, **kwargs):
    
    if created:
        try:
            Profile.objects.create(username=instance)
        except:
            pass

# @receiver(post_save, sender=Model)
# def _post_save_receiver(sender, **kwargs):
#     pass
