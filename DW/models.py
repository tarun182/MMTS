from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from users.models import CustomUser
from django.utils import timezone
    
from decimal import Decimal
User = settings.AUTH_USER_MODEL

class Deposit(models.Model):
    #account_id=  models.OneToOneField(account_id, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='deposits',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('10.00'))
        ]
    )
    timestamp   = models.DateTimeField(auto_now_add=True)
    #timestamp = models.DateTimeField(blank=False,default=timezone.now)


    def __str__(self):
        return str(self.user.account_id)

class Withdraw(models.Model):
    user = models.ForeignKey(
        User,
        related_name='withdrawals',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('10.00'))
        ]
    )

    timestamp   = models.DateTimeField(auto_now_add=True)
    #timestamp = models.DateTimeField(blank=False,default=timezone.now)
    
    def __str__(self):
        return str(self.user.account_id)