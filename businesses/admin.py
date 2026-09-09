from django.contrib import admin
from .models import Business, Transaction, FinancialPosition

#Setting up django admin by registering the classes mentioned in the models file, which helps in managing the database records through its admin panel
admin.site.register(Business)
admin.site.register(Transaction)
admin.site.register(FinancialPosition)