def calculate_profit_margin(profit, revenue):

    if revenue == 0:
        return 0

    return (profit / revenue) * 100


def calculate_expense_ratio(expenses, revenue):

    if revenue == 0:
        return 0

    return (expenses / revenue) * 100


def calculate_revenue_growth(current_revenue, previous_revenue):

    if previous_revenue == 0:
        return 0

    return (
        (current_revenue - previous_revenue)
        / previous_revenue
    ) * 100


def calculate_expense_growth(current_expenses, previous_expenses):

    if previous_expenses == 0:
        return 0

    return (
        (current_expenses - previous_expenses)
        / previous_expenses
    ) * 100


def calculate_current_ratio(current_assets, current_liabilities):

    if current_liabilities == 0:
        return 0

    return current_assets / current_liabilities


def calculate_receivables_ratio(receivables, revenue):

    if revenue == 0:
        return 0

    return (receivables / revenue) * 100