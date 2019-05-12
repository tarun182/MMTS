from django import forms

from .models import Deposit, Withdraw, Transfer

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ["amount"]

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ["amount"]
    
    # Validation has to be done

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ["sender_id","amount"]