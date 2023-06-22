import calendar

def calculate_emi(principal, tenure, interest_rate):
    
    interest_rate = interest_rate / 100

    
    monthly_interest_rate = interest_rate / 12

    
    num_of_months = tenure * 12

    
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** num_of_months) / (
            (1 + monthly_interest_rate) ** num_of_months - 1)

    return emi



principal = float(input("Enter the principal amount: "))
tenure = int(input("Enter the tenure (in years): "))
interest_rate = float(input("Enter the interest rate: "))


emi = calculate_emi(principal, tenure, interest_rate)


print("Month\tYear\t\tPrincipal\tInterest\tTotal Payment\tBalance")
balance = principal
total_payment = 0
for year in range(1, tenure + 1):
    for month in range(1, 13):
        interest = balance * interest_rate / 100
        principal_payment = emi - interest
        balance -= principal_payment
        total_payment += emi

        month_name = calendar.month_name[month]
        print(f"{month_name}\t{year}\t\t{round(principal_payment, 2)}\t\t{round(interest, 2)}\t\t{round(emi, 2)}\t\t{round(balance, 2)}")

print("Loan Paid To Date:", round(total_payment, 2))
