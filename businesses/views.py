from django.shortcuts import render, get_object_or_404

from .models import Business
from backend.integrating_financial_analysis.final_analysis import analyze_business

def dashboard(request, business_id):

    business = get_object_or_404 (Business,id=business_id)

    analysis = analyze_business (business)

    context = {"business": business, "analysis": analysis}

    return render(request, "dashboard.html", context)
