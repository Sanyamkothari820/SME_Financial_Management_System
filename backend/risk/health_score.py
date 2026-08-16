def calculate_health_score(cashflow_score, revenue_growth_score, expense_score, debt_score, receivables_score, profitability_score):

    score = (cashflow_score + revenue_growth_score + expense_score + debt_score + receivables_score + profitability_score)

    return score


def health_status(score):

    if score >= 80:
        return "Healthy"

    elif score >= 60:
        return "Moderate"

    elif score >= 40:
        return "At Risk"

    else:
        return "Critical"