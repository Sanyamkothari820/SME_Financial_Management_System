def check_profit_margin(profit_margin):

    if profit_margin < 0:
        return "CRITICAL: Business is operating at a loss."

    elif profit_margin < 5:
        return "WARNING: Profit margin is very low."

    elif profit_margin < 10:
        return "WATCH: Profit margin is below the preferred level."

    return None


def check_expense_ratio(expense_ratio):

    if expense_ratio > 90:
        return "CRITICAL: Expenses are consuming most of the revenue."

    elif expense_ratio > 80:
        return "WARNING: Expense ratio is very high."

    elif expense_ratio > 70:
        return "WATCH: Operating expenses are relatively high."

    return None


def check_revenue_growth(revenue_growth):

    if revenue_growth < -10:
        return "CRITICAL: Revenue has declined significantly."

    elif revenue_growth < 0:
        return "WARNING: Revenue is declining."

    elif revenue_growth < 5:
        return "WATCH: Revenue growth is weak."

    return None


def check_expense_growth(expense_growth):

    if expense_growth > 30:
        return "CRITICAL: Expenses are increasing rapidly."

    elif expense_growth > 20:
        return "WARNING: Expense growth is unusually high."

    elif expense_growth > 10:
        return "WATCH: Expenses are growing significantly."

    return None


def check_growth_gap(revenue_growth, expense_growth):

    if expense_growth - revenue_growth > 15:
        return (
            "WARNING: Expenses are growing much faster "
            "than revenue."
        )

    return None


def check_current_ratio(current_ratio):

    if current_ratio < 0.75:
        return "CRITICAL: Severe short-term liquidity risk."

    elif current_ratio < 1:
        return "WARNING: Current liabilities exceed current assets."

    elif current_ratio < 1.2:
        return "WATCH: Short-term liquidity is relatively weak."

    return None


def check_receivables_ratio(receivables_ratio):

    if receivables_ratio > 40:
        return "CRITICAL: Very high proportion of revenue is tied up in receivables."

    elif receivables_ratio > 30:
        return "WARNING: Receivables are significantly high."

    elif receivables_ratio > 20:
        return "WATCH: Receivables require monitoring."

    return None


def evaluate_financial_risks(ratios):

    warnings = []

    warning = check_profit_margin(
        ratios["profit_margin"]
    )

    if warning:
        warnings.append(warning)

    warning = check_expense_ratio(
        ratios["expense_ratio"]
    )

    if warning:
        warnings.append(warning)

    warning = check_revenue_growth(
        ratios["revenue_growth"]
    )

    if warning:
        warnings.append(warning)

    warning = check_expense_growth(
        ratios["expense_growth"]
    )

    if warning:
        warnings.append(warning)

    warning = check_growth_gap(
        ratios["revenue_growth"],
        ratios["expense_growth"]
    )

    if warning:
        warnings.append(warning)

    warning = check_current_ratio(
        ratios["current_ratio"]
    )

    if warning:
        warnings.append(warning)

    warning = check_receivables_ratio(
        ratios["receivables_ratio"]
    )

    if warning:
        warnings.append(warning)

    return warnings