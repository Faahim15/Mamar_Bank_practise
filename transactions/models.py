from django.db import models
from accounts.models import UserBankAccount
from django.contrib.auth.models import User
from .constants import TRANSACTION_TYPE

class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name = 'transactions', on_delete = models.CASCADE) # ekjon user er multiple transactions hote pare
    
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    
    
    class Meta:
        ordering = ['timestamp'] 

class Money_transfer_Model(models.Model):
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sent_transactions')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'received_transactions') 
    amount = models.DecimalField(max_digits = 12, decimal_places = 2) 
    date = models.DateTimeField(auto_now_add = True) 

    def __str__(self):
        return f'Sender: {str(self.sender.username)}'  
    

