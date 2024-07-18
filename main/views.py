from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from currencyValues.models import Currency
from .forms import CurrencyForm

@login_required
def currency_list(request):
    currencies = Currency.objects.all()
    return render(request, 'index.html', {'currencies': currencies})

@login_required
def currency_create(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('currency-list')
    else:
        form = CurrencyForm()
    return render(request, 'currency_form.html', {'form': form})

@login_required
def currency_edit(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        form = CurrencyForm(request.POST, instance=currency)
        if form.is_valid():
            form.save()
            return redirect('currency-list')
    else:
        form = CurrencyForm(instance=currency)
    return render(request, 'currency_form.html', {'form': form})

@login_required
def currency_delete(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        currency.delete()
        return redirect('currency-list')
    return render(request, 'currency_confirm_delete.html', {'currency': currency})

