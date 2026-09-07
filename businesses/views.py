from django.shortcuts import render, get_object_or_404

from .models import Business
from backend.integrating_financial_analysis.final_analysis import analyze_business


def dashboard(request, business_id):

    business = get_object_or_404(
        Business,
        id=business_id
    )

    analysis = analyze_business(business)

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
    }

    return render(
        request,
        "dashboard.html",
        context
    )