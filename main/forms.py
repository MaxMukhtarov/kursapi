from django import forms
from currencyValues.models import Currency

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['code', 'sell_rate', 'buy_rate']