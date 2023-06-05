from django.db import models
from django.utils import timezone

VOUCHER_CHOICES = (
    ('GV', 'General Voucher'),
    ('PV', 'Payment Voucher'),
    ('RV', 'Receipt Voucher'),
)
# table/model for account types
class account_type(models.Model):
    account_type_name = models.CharField(max_length=100)

    def __str__(self) :
        return self.account_type_name
    
class main_account(models.Model):
    account_type = models.ForeignKey(account_type, on_delete=models.CASCADE, related_name='main')
    main_acount_name = models.CharField(max_length=100)

    def __str__(self) :
        return self.main_acount_name

from django.db import models
from django.utils import timezone

class SubAccount(models.Model):
    sub_account_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    customer_website = models.CharField(max_length=100)
    opening_balance = models.IntegerField()
    main_account = models.ForeignKey('main_account', on_delete=models.CASCADE, null=True, blank=True, related_name='customer_account')

    def __str__(self) :
        return self.sub_account_name

    def save(self, *args, **kwargs):
        is_credit = True  # Default to credit
        if self.opening_balance < 0:
            is_credit = False  # Set as debit if the opening balance is negative

        super().save(*args, **kwargs)

        # Create a ledger entry for the opening balance
        Ledger.objects.create(
            account=self,
            date=timezone.now(),
            ref_no='Opening Balance',
            type='Credit' if self.opening_balance > 0 else 'Debit',
            description='Opening Balance',
            credit=self.opening_balance if self.opening_balance > 0 else 0,
            debit=self.opening_balance if not self.opening_balance > 0 else 0
        )


class Customer(models.Model):

    customer_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone1 = models.CharField(max_length=15, null=True, blank=True)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    customer_website  = models.CharField(max_length=100, null=True, blank=True)
    account = models.ForeignKey(account_type, on_delete=models.CASCADE, null=True, blank=True, related_name='customer_account')

    def __str__(self) :
        return self.customer_name


class Vendor(models.Model):

    vendor_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone1 = models.CharField(max_length=15, null=True, blank=True)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    vendor_website = models.CharField(max_length=100, null=True, blank=True)
    account = models.ForeignKey(account_type, on_delete=models.CASCADE, null=True, blank=True,  related_name='vendor_account')

    def __str__(self) :
        return self.vendor_name

class ProductCategories(models. Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) :
        return self.category_name

class Product(models.Model):
    product = models.ForeignKey(ProductCategories, on_delete=models.CASCADE, related_name='product_category')
    product_name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) :
        return self.product_name

class Invoice(models.Model):
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_invoice')
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields related to the invoice master
    def __str__(self) :
        return self.invoice_number

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items', null=True, blank=True)

    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Voucher(models.Model):
    
    voucher_date = models.DateTimeField(default=timezone.now)
    voucher_type = models.CharField(max_length=2, choices=VOUCHER_CHOICES)
    voucher_description = models.CharField(max_length=200)

class VoucherDetail(models.Model):
    account = models.ForeignKey(SubAccount, on_delete=models.CASCADE, related_name='detail')
    description = models.CharField(max_length=200)
    credit = models.DecimalField(max_digits=15, decimal_places=2)
    debit = models.DecimalField(max_digits=15, decimal_places=2)

class Ledger(models.Model):
    account = models.ForeignKey(SubAccount, on_delete=models.CASCADE, related_name='ledger')
    date = models.DateTimeField(default=timezone.now)
    ref_no = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    credit = models.DecimalField(max_digits=15, decimal_places=2)
    debit = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self) :
        return self.type


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_product', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    ref_no = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    qty_in = models.IntegerField(max_length=5, null=True, blank=True)
    qty_out = models.IntegerField(max_length=5, null=True, blank=True)   

    def __str__(self) :
        return self.product



class PurchaseInvoice(models.Model):
    vendor =  models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_invoice')
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields related to the invoice master
    def __str__(self) :
        return self.invoice_number
    
class PurchaseInvoiceItem(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE, related_name='purchase_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase_product', null=True, blank=True)

    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)