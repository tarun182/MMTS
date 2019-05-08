from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import DepositForm,WithdrawForm,TransferForm
from users.models  import *
from .models import Transfer

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

def transfer_view(request):
    form = TransferForm(request.POST or None)

    if form.is_valid():
        transfer= form.save(commit=False)
        transfer.user=request.user
        transfer.save()
        transfer.user.balance-=transfer.amount
        send_obj=CustomUser.objects.get(account_id=transfer.sender_id)
        send_obj.balance+=transfer.amount
        transfer.user.save()
        send_obj.save()
        messages.success(request, 'You Have Sent Money .'.format(transfer.amount))
        return redirect("home")

    context = {
        "title": "Transfer",
        "form": form
    }
    return render(request, "DW/DW.htm", context)

