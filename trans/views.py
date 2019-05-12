from django.shortcuts import render
from DW.models import Withdraw,Deposit,Transfer
from DW.models import *


def trans(request):
    user = request.user
    dep_obj  = Deposit.objects.filter(user=user)
    with_obj = Withdraw.objects.filter(user=user)
    Td_obj   = Transfer.objects.filter(user=user)
    Tc_obj   = Transfer.objects.filter(sender_id=user.account_id)

    context={
        'dep_obj':dep_obj,
        'with_obj':with_obj,
        'Td_obj':Td_obj,
        'Tc_obj':Tc_obj,
    }

    return render(request,'Trans/trans.htm', context)


def mini(request):
    user = request.user
    dep_obj  = Deposit.objects.filter(user=user)
    with_obj = Withdraw.objects.filter(user=user)
    Td_obj   = Transfer.objects.filter(user=user)
    Tc_obj   = Transfer.objects.filter(sender_id=user.account_id)

    context={
        'dep_obj':dep_obj,
        'with_obj':with_obj,
        'Td_obj':Td_obj,
        'Tc_obj':Tc_obj,
    }

    return render(request,'Trans/mini.htm', context)
