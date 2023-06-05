from django.contrib import admin
import myapp.models

admin.site.register(myapp.models.account_type)
admin.site.register(myapp.models.main_account)
admin.site.register(myapp.models.Customer)
admin.site.register(myapp.models.Vendor)
admin.site.register(myapp.models.Product)
admin.site.register(myapp.models.ProductCategories)
admin.site.register(myapp.models.Inventory)
admin.site.register(myapp.models.SubAccount)
admin.site.register(myapp.models.Ledger)
