def check_negative_cashflow(cashflow):

    if cashflow < 0:

        return {
            "severity": "HIGH",
            "message": "Negative cashflow detected."
        }

    return None


def check_expense_growth(revenue_growth, expense_growth
):

    if expense_growth > revenue_growth:

        return {
            "severity": "MEDIUM",
            "message":
                "Expenses are growing faster than revenue."
        }

    return None


def check_receivables_growth(receivables_growth):

    if receivables_growth > 20:

        return {
            "severity": "MEDIUM",
            "message":
                "Receivables have increased significantly."
        }

    return None


def generate_warnings(metrics):

    warnings = []

    warning = check_negative_cashflow(
        metrics["cashflow"]
    )

    if warning:
        warnings.append(warning)

    warning = check_expense_growth(
        metrics["revenue_growth"],
        metrics["expense_growth"]
    )

    if warning:
        warnings.append(warning)

    return warnings