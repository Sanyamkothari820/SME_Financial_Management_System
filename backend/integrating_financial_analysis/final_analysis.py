from analytics.calculations import *
from analytics.ratios import *
from risk.health_score import *
from risk.rules import *
from transactions.models import Transaction, FinancialPosition

def analyze_business(business):


    transactions = Transaction.objects.filter(business= business)

    financial_position = FinancialPosition.objects.filter(business=business).latest("date")

    revenue = calc_revenue(transactions)
    expenses = calc_expenses(transactions)

    profit = calc_profit(revenue, expenses)

    monthly_financials = calc_monthly_financials(transactions)

    if len(monthly_financials) < 2:

        revenue_growth = 0
        expense_growth = 0

    else:
    
        current_revenue = monthly_financials.iloc[-1]["revenue"]
        previous_revenue = monthly_financials.iloc[-2]["revenue"]

        current_expenses = monthly_financials.iloc[-1]["expenses"]
        previous_expenses = monthly_financials.iloc[-2]["expenses"]

    current_assets = calc_current_assets(financial_position)
    current_liabilities = calc_current_liabilities(financial_position)

    receivables = calc_receivables(financial_position)

    profit_margin = calculate_profit_margin(
        profit,
        revenue
    )

    expense_ratio = calculate_expense_ratio(
        expenses,
        revenue
    )

    revenue_growth = calculate_revenue_growth(
        current_revenue,
        previous_revenue
    )

    expense_growth = calculate_expense_growth(
        current_expenses,
        previous_expenses
    )

    current_ratio = calculate_current_ratio(
        current_assets,
        current_liabilities
    )

    receivables_ratio = calculate_receivables_ratio(
        receivables,
        revenue
    )

    ratios = {
        "profit_margin": profit_margin,
        "expense_ratio": expense_ratio,
        "revenue_growth": revenue_growth,
        "expense_growth": expense_growth,
        "current_ratio": current_ratio,
        "receivables_ratio": receivables_ratio
    }

    warnings = evaluate_financial_risks(ratios)

    ind_scores = {
    "profit_margin": profitability_score(
        ratios["profit_margin"]
    ),

    "expense_ratio": expense_score(
        ratios["expense_ratio"]
    ),

    "revenue_growth": revenue_growth_score(
        ratios["revenue_growth"]
    ),

    "expense_growth": expense_growth_score(
        ratios["expense_growth"]
    ),

    "current_ratio": liquidity_score(
        ratios["current_ratio"]
    ),

    "receivables_ratio": receivables_score(
        ratios["receivables_ratio"]
    )
}

    
    health_score = calc_health_score(ind_scores)

    status = health_status(health_score)

    return {
        "financial_data": {
            "revenue": revenue,
            "expenses": expenses,
            "profit": profit
        },
        "ratios": ratios,
        "ind_scores": ind_scores,
        "health_score": health_score,
        "health_status": status,
        "warnings": warnings
    }


