from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import DepositForm,WithdrawForm

def deposit_view(request):
    form = DepositForm(request.POST or None)

    if form.is_valid():
        deposit = form.save(commit=False)
        deposit.user = request.user
        deposit.save()
        deposit.user.balance += deposit.amount
        deposit.user.save()
        messages.success(request, 'You Have Deposited .'.format(deposit.amount))
        return redirect("home")

    context = {
        "title": "Deposit",
        "form": form
    }
    return render(request, "DW/DW.htm", context)

def withdraw_view(request):
    form = WithdrawForm(request.POST or None)

    if form.is_valid():
        withdraw= form.save(commit=False)
        withdraw.user=request.user
        withdraw.save()
        withdraw.user.balance-=withdraw.amount
        withdraw.user.save()
        messages.success(request, 'You Have Withdrawn .'.format(withdraw.amount))
        return redirect("home")

    context = {
        "title": "Withdraw",
        "form": form
    }
    return render(request, "DW/DW.htm", context)

def trans(request):
    dep_obj  = Withdraw.objects.all()
    with_obj = Deposit.objects.all()

    context={
        'dep_obj':dep_obj,
        'with_obj':with_obj,
    }

    return render(request,'Trans/trans.htm', context)