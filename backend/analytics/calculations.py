import pandas as pd
# data = [1,2,3,4,5]
def calc_revenue(transactions):

    revenue = 0
    for transaction in transactions:

        if transaction.transaction_type == "revenue":
            revenue += transaction.amount

    return revenue


def calc_expenses(transactions):

    expenses = 0
    for transaction in transactions:
        if transaction.transaction_type == "expenses":

            expenses += transaction.amount

    return expenses


def calc_cashflow(cash_inflow, cash_outflow):

    return cash_inflow - cash_outflow



def calc_profit(revenue, expenses):
    
    profit = revenue -expenses

    return profit


def calc_revenue_by_category(transactions):

    total = {}
    for transaction in transactions:

        if transaction.transaction_type == "revenue":

            category = transaction.category

            if category not in total:
                total[category] = 0

            total[category] += transaction.amount

    return total

def calc_expenses_by_category(transactions):

    total = {} 
    for transaction in transactions:

        if transaction.transaction_type == "expenses":

            category = transaction.category

            if category not in total:
                total[category] = 0

            total[category] += transaction.amount

    return total     
    
def calc_monthly_financials(data):

    data["date"] = pd.to_datetime(data["date"])

    data["month"] = data["date"].dt.to_period("M")

    monthly_revenue = (
        data[data["transaction_type"] == "revenue"]
        .groupby("month")["amount"]
        .sum()
    )

    monthly_expenses = (
        data[data["transaction_type"] == "expenses"]
        .groupby("month")["amount"]
        .sum()
    )

    result = pd.DataFrame({
        "revenue": monthly_revenue,
        "expenses": monthly_expenses
    }).fillna(0)

    result["profit"] = result["revenue"]- result["expenses"]

    return result

def calculate_revenue_change(current, previous):
    return current - previous

def calculate_expense_change(current, previous):
    return current - previous

def calculate_current_assets(financial_position):

    return (financial_position.cash + financial_position.bank_balance + financial_position.receivables + financial_position.inventory + financial_position.other_current_assets)

def calculate_current_liabilities(financial_position):

    return (financial_position.accounts_payable + financial_position.short_term_debt + financial_position.other_current_liabilities)

def calculate_receivables(financial_position):

    return financial_position.receivables