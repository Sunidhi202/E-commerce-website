from django.contrib import admin
from users.models import (Profile,
                         Order,
                         OrderItem,
                         ShippingAddress,
                         MyUser)

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(MyUser)

