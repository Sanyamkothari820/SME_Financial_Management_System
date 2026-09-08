#Scoring the profitability of the business
def profitability_score(profit_margin):

    if profit_margin >= 20:
        return 100
    elif profit_margin >= 15:
        return 85
    elif profit_margin >= 10:
        return 70
    elif profit_margin >= 5:
        return 50
    elif profit_margin >= 0:
        return 30
    else:
        return 0


#Scoring the expense management of the business
def expense_score(expense_ratio):

    if expense_ratio <= 50:
        return 100
    elif expense_ratio <= 60:
        return 85
    elif expense_ratio <= 70:
        return 70
    elif expense_ratio <= 80:
        return 50
    elif expense_ratio <= 90:
        return 30
    else:
        return 10


#Scoring the revenue growth of the business between two timespan
def revenue_growth_score(revenue_growth):

    if revenue_growth >= 20:
        return 100
    elif revenue_growth >= 10:
        return 85
    elif revenue_growth >= 5:
        return 70
    elif revenue_growth >= 0:
        return 60
    elif revenue_growth >= -10:
        return 40
    else:
        return 20


#Scoring the expense growth of the business between two timespan
def expense_growth_score(expense_growth):

    if expense_growth <= 0:
        return 100
    elif expense_growth <= 5:
        return 85
    elif expense_growth <= 10:
        return 70
    elif expense_growth <= 20:
        return 50
    elif expense_growth <= 30:
        return 30
    else:
        return 10


#Scoring the liquidity of the business 
def liquidity_score(current_ratio):

    if current_ratio >= 2:
        return 100
    elif current_ratio >= 1.5:
        return 85
    elif current_ratio >= 1.2:
        return 70
    elif current_ratio >= 1:
        return 50
    elif current_ratio >= 0.75:
        return 30
    else:
        return 10


#Scoring the amount required to be collected by the business 
def receivables_score(receivables_ratio):

    if receivables_ratio <= 5:
        return 100
    elif receivables_ratio <= 10:
        return 85
    elif receivables_ratio <= 20:
        return 70
    elif receivables_ratio <= 30:
        return 50
    elif receivables_ratio <= 40:
        return 30
    else:
        return 10




def calc_health_score(ind_scores):
    '''
    Here individual health scores is taken as arguments.
    Then, calculating the health score by multiplying the individual health score with the individual weights and
    adding all the individual weights as a compounded health score, returning the health score as output
    '''


    weights = {
        "profit_margin": 0.20,
        "expense_ratio": 0.15,
        "revenue_growth": 0.20,
        "expense_growth": 0.15,
        "current_ratio": 0.20,
        "receivables_ratio": 0.10
    }

    score = (
        ind_scores["profit_margin"] * weights["profit_margin"]
        + ind_scores["expense_ratio"] * weights["expense_ratio"]
        + ind_scores["revenue_growth"] * weights["revenue_growth"]
        + ind_scores["expense_growth"] * weights["expense_growth"]
        + ind_scores["current_ratio"] * weights["current_ratio"]
        + ind_scores["receivables_ratio"] * weights["receivables_ratio"]
    )

    return score





def health_status(score):
    '''
    Assigning the health status of the business on the basis of the health score achieved by the company.
    Here health score is taken as an argument and returns the status of the business as output
    '''

    if score >= 80:
        return "Healthy"

    elif score >= 60:
        return "Moderate"

    elif score >= 40:
        return "At Risk"

    else:
        return "Critical"