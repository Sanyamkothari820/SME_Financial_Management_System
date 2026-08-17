from analytics.calculations import *
from analytics.ratios import *
from risk.health_score import *
from risk.rules import *


def analyze_business(data):


    revenue = calc_revenue(data)
    expenses = calc_expenses(data)

    profit = calc_profit(revenue, expenses)

    current_revenue = data["current_revenue"]
    previous_revenue = data["previous_revenue"]

    current_expenses = data["current_expenses"]
    previous_expenses = data["previous_expenses"]

    current_assets = data["current_assets"]
    current_liabilities = data["current_liabilities"]

    receivables = data["receivables"]

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


