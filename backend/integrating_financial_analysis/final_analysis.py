
# Importing the backend calculations file for final analysis, calculations and calling purpose

from backend.analytics.calculations import *
from backend.analytics.ratios import *
from backend.risk.health_score import *
from backend.risk.rules import *

#Importing the django model classes for the calculations
from businesses.models import Transaction, FinancialPosition,Business




# Main function from where everything is orchestrated
def analyze_business(business):


    '''
     This function is used for calling all the financial attributes, functions, status, scores and warnings which has been already calculated  in the seperate files according to their requirements
     It takes the name of the business as an argument and use that name for further assessment and calculations
     It calls and returns all the financial values including the revenue, expenses, profit, monthly financial for trends, charts and various other graphs, all the current assets, liabilities and receivables to collect
     It calls and returns all the financial ratios including the profit margin, expense growth, revenue growth, receivable ratio, current ratio and expense ratio
     It warns the business for the declining activities occuring in the business
     It evaluates the health score and status of the business
     At last it returns all the  financial values and information to the business owner or the accountant depending upon who is using the system

    '''



# Telling the django database to give the transactions that belong to the particular business
    transactions = Transaction.objects.filter(business= business)


# Telling the django database to find the financial-position belonging to this business, then select the most recent one based on the date
    financial_position = FinancialPosition.objects.filter(business=business).latest("date")



    revenue = calc_revenue(transactions)
    expenses = calc_expenses(transactions)
    profit = calc_profit(revenue, expenses)
    monthly_financials = calc_monthly_financials(transactions)




# If the transaction has less than two months it is not possible to calculate the current and previous revenue and expenses along with revenue and expense growth
    if len(monthly_financials) < 2:

        revenue_growth = 0
        expense_growth = 0



    else:
    
        current_revenue = monthly_financials.iloc[-1]["revenue"]
        previous_revenue = monthly_financials.iloc[-2]["revenue"]


        current_expenses = monthly_financials.iloc[-1]["expenses"]
        previous_expenses = monthly_financials.iloc[-2]["expenses"]


        revenue_growth = calculate_revenue_growth(current_revenue,previous_revenue)
        expense_growth = calculate_expense_growth(current_expenses, previous_expenses)



    current_assets = calc_current_assets(financial_position)
    current_liabilities = calc_current_liabilities(financial_position)
    receivables = calc_receivables(financial_position)



    profit_margin = calculate_profit_margin(profit, revenue)

    expense_ratio = calculate_expense_ratio(expenses, revenue)

    current_ratio = calculate_current_ratio(current_assets,  current_liabilities)

    receivables_ratio = calculate_receivables_ratio(receivables, revenue)



    ratios = {
        "profit_margin": profit_margin,
        "expense_ratio": expense_ratio,
        "revenue_growth": revenue_growth,
        "expense_growth": expense_growth,
        "current_ratio": current_ratio,
        "receivables_ratio": receivables_ratio
    }

# Calling the evaluate_financial_risks for warning the negative activities occuring in the business
    warnings = evaluate_financial_risks(ratios)




    ind_scores = {

    "profit_margin": profitability_score(ratios["profit_margin"]),

    "expense_ratio": expense_score(ratios["expense_ratio"] ),

    "revenue_growth": revenue_growth_score(ratios["revenue_growth"]),

    "expense_growth": expense_growth_score(ratios["expense_growth"]),

    "current_ratio": liquidity_score(ratios["current_ratio"]),

    "receivables_ratio": receivables_score(ratios["receivables_ratio"])

}

 # Calling the calc_health_score for calculating the health score of the business and assigning it to the variable to understand where it is heading    
    health_score = calc_health_score(ind_scores)



# Calling the health_status for understanding the health status of the business and assigning it to the variable
    status = health_status(health_score)



#Returning the values generated from the calculations onto the dashboard to the required authority
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



#Ignore it, just to check whether the system is working manually or not which will be managed in further time
# result = analyze_business(Business.objects.get(name="ABC Traders"))
# print(result)