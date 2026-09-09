from django.db import models


class Business(models.Model):

    '''
     Creating the Business class which should contain various info about the business including its name, industry and the date at which it is created
    '''

    name = models.CharField(
        max_length=200
    )

    industry = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):

    ''' 
    Creating the Transaction class which should contain various info about the transaction records including the name of the business, the date at which it is created, the type of the transactions, its category, the amount which is associated with it along with the description of the transactions
    '''


    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    date = models.DateField()

    transaction_type = models.CharField(
        max_length=20
    )

    category = models.CharField(
        max_length=100
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"


class FinancialPosition(models.Model):

    ''' Creating the FinancialPosition class which should contain various info about the financial status of the business including the name of the business, the date at which it is created, its financial attributes which includes cash, bank balance, receivables, inventory, other current assets, account payable, short-term debt and other current liabilities
    '''

    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="financial_positions"
    )

    date = models.DateField()

    cash = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    bank_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    receivables = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    inventory = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    other_current_assets = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    accounts_payable = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    short_term_debt = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    other_current_liabilities = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"{self.business.name} - {self.date}"
