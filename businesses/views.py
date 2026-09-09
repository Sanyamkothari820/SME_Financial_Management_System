from django.shortcuts import render, get_object_or_404

from .models import Business, Transaction
from backend.integrating_financial_analysis.final_analysis import analyze_business
from backend.analytics.calculations import calc_monthly_financials


def dashboard(request, business_id):

    '''
        This function takes business_id along with the request as input arguments, and by using that id, it tells the django to find the business with the id and then calls the analyze_business function with that particular business name and returns the request along with its content in the dashboard of the websites
        
    '''

    business = get_object_or_404(
        Business,
        id=business_id
    )

    analysis = analyze_business(business)

    transactions = Transaction.objects.filter(
        business=business
    )

    monthly_financials = calc_monthly_financials(transactions)

    monthly_data = []

    for month, row in monthly_financials.iterrows():

        monthly_data.append({
            "month": str(month),
            "revenue": float(row["revenue"]),
            "expenses": float(row["expenses"]),
        })

    context = {
        "business": business,

        "revenue": analysis["financial_data"]["revenue"],
        "expenses": analysis["financial_data"]["expenses"],
        "profit": analysis["financial_data"]["profit"],

        "profit_margin": analysis["ratios"]["profit_margin"],
        "expense_ratio": analysis["ratios"]["expense_ratio"],
        "revenue_growth": analysis["ratios"]["revenue_growth"],
        "expense_growth": analysis["ratios"]["expense_growth"],
        "current_ratio": analysis["ratios"]["current_ratio"],
        "receivables_ratio": analysis["ratios"]["receivables_ratio"],

        "health_score": analysis["health_score"],
        "health_status": analysis["health_status"],

        "warnings": analysis["warnings"],

        "monthly_data": monthly_data,
    }

    return render(
        request,
        "dashboard.html",
        context
    )

