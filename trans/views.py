from django.shortcuts import render
from DW.models import Withdraw,Deposit

def trans(request):
    user = request.user
    dep_obj  = Deposit.objects.filter(user=user)
    with_obj = Withdraw.objects.filter(user=user)

    context={
        'dep_obj':dep_obj,
        'with_obj':with_obj,
    }

    return render(request,'Trans/trans.htm', context)

