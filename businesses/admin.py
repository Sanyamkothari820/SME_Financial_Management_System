from django.contrib import admin
from .models import Business, Transaction, FinancialPosition

admin.site.register(Business)
admin.site.register(Transaction)
admin.site.register(FinancialPosition)