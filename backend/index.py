def user_input(bns,rvn,exp):
    print("Enterprise Name:",bns)
    print("Revenue Earned: Rs",rvn)
    print("Expenditure Incurred: Rs",exp)

business_name = input("Enter the name of the company:")
revenue = float(input("Enter the revenue earned by the company:"))
expense = float(input("Enter the expense incurred by the company:"))

user_input(business_name,revenue,expense)

cashflow = revenue - expense

def cashflow_calc(cashflow):
    if cashflow>0:
        print("The company has positive cashflow")
    elif cashflow<0:
        print("The company has negative cashflow")
    else:
        print("The company is in breakeven conditon")

cashflow_calc(cashflow)
print("Net Cashflow: ",cashflow)
