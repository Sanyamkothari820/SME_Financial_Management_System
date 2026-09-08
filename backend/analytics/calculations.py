import pandas as pd



# Calculating the revenue from the transactions 
def calc_revenue(transactions):

    revenue = 0
    for transaction in transactions:

        if transaction.transaction_type == "revenue": #transaction_type is an attribute in the transactions
            revenue += transaction.amount

    return revenue




#  Calculating the expenses from the transactions 
def calc_expenses(transactions):

    expenses = 0
    for transaction in transactions:
        if transaction.transaction_type == "expenses":

            expenses += transaction.amount

    return expenses




#  Calculating the cashflow of the business 
def calc_cashflow(cash_inflow, cash_outflow):

    return cash_inflow - cash_outflow



#  Calculating the profit from the transactions 
def calc_profit(revenue, expenses):
    
    profit = revenue -expenses

    return profit



#  Calculating the revenue through each category 
def calc_revenue_by_category(transactions):

    total = {}
    for transaction in transactions:

        if transaction.transaction_type == "revenue":

            category = transaction.category

            if category not in total:
                total[category] = 0

            total[category] += transaction.amount

    return total



#  Calculating the expenses through each category
def calc_expenses_by_category(transactions):

    total = {} 
    for transaction in transactions:

        if transaction.transaction_type == "expenses":

            category = transaction.category

            if category not in total:
                total[category] = 0

            total[category] += transaction.amount

    return total     



# Calculating the monthly financial for trends and charts
def calc_monthly_financials(transactions):

    data = []

    for transaction in transactions:

        data.append({
            "date": transaction.date,
            "transaction_type": transaction.transaction_type,
            "amount": float(transaction.amount)
        })

    data = pd.DataFrame(data)

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


# Calculating the change in revenue for analysis
def calc_revenue_change(current, previous):
    return current - previous


# Calculating the change in expenses for analysis
def calc_expense_change(current, previous):
    return current - previous


# Calculating the current assets available
def calc_current_assets(financial_position):

    return (financial_position.cash + financial_position.bank_balance + financial_position.receivables + financial_position.inventory + financial_position.other_current_assets)


# Calculating the current liabilities available
def calc_current_liabilities(financial_position):

    return (financial_position.accounts_payable + financial_position.short_term_debt + financial_position.other_current_liabilities)


# Calculating the receivables required to collect
def calc_receivables(financial_position):

    return financial_position.receivables