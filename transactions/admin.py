from django.contrib import admin

from .models import (PurchaseBill, PurchaseBillDetails, PurchaseItem, SaleBill,
                     SaleBillDetails, SaleItem, Supplier)

admin.site.register(Supplier)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)
admin.site.register(PurchaseBillDetails)
admin.site.register(SaleBill)
admin.site.register(SaleItem)
admin.site.register(SaleBillDetails)
