from django import forms
from .models import main_account, account_type, SubAccount

class MainAccountForm(forms.ModelForm):
    account_type = forms.ModelChoiceField(queryset=account_type.objects.all())

    class Meta:
        model = main_account
        fields = ['account_type', 'main_acount_name']
        labels = {
            'account_type': 'Account Type',
            'main_acount_name': 'Main Account Name',
        }

    def __init__(self, *args, **kwargs):
        super(MainAccountForm, self).__init__(*args, **kwargs)
        

        # Example: Customize the account_type field widget
        self.fields['account_type'].widget.attrs['class'] = 'form-control'

        # Example: Add a placeholder for the main_acount_name field
        self.fields['main_acount_name'].widget.attrs['class'] = 'form-control'


class SubAccountForm(forms.ModelForm):
        
   # main_account = forms.ChoiceField(
    #    choices=[(account.pk, account.main_acount_name) for account in main_account.objects.all()], label='Main Account', required=True)
    main_account = forms.ModelChoiceField(queryset=main_account.objects.all(), label='Main Account', required=True)
    sub_account_name = forms.CharField(label='Sub Account Name', required=True)
    address = forms.CharField(label='Address', required=False)
    city = forms.CharField(label='City', required=False)
    city = forms.CharField(label='City', required=False)
    email = forms.EmailField(label='Email', required=False)
    phone1 = forms.CharField(label='Phone 1', required=False)
    phone2 = forms.CharField(label='Phone 2', required=False)
    customer_website = forms.CharField(label='Customer Website', required=False)
    opening_balance = forms.IntegerField(label='Opening Balance', required=False)
    #is_credit = forms.BooleanField(label='Is Credit')

    class Meta:
        model = SubAccount
        fields = [
            'main_account',
            'sub_account_name',
            'address',
            'city',
            'email',
            'phone1',
            'phone2',
            'customer_website',
            'opening_balance'
            #'is_credit'
            
        ]
        
    def __init__(self, *args, **kwargs):
        super(SubAccountForm, self).__init__(*args, **kwargs)

        self.fields['main_account'].widget.attrs['class'] = 'form-control'
        self.fields['sub_account_name'].widget.attrs['class'] = 'form-control' 
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone1'].widget.attrs['class'] = 'form-control'
        self.fields['phone2'].widget.attrs['class'] = 'form-control'
        self.fields['customer_website'].widget.attrs['class'] = 'form-control'
        self.fields['opening_balance'].widget.attrs['class'] = 'form-control'
        self.fields['opening_balance'].widget.attrs['placeholder'] = 'Use ( - ) for Debit'
        self.fields['opening_balance'].widget.attrs['value'] = 0
        #self.fields['is_credit'].widget.attrs['class'] = 'form-check-input'
        #self.fields['is_credit'].widget.attrs['type'] = 'radio'

    
