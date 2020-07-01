import is_str_float

class Compound_Cal:
    def __init__(self, principal, interest_rate, compound_rate, years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.compound_rate = compound_rate
        self.years = years


def input_cal():

    principal = input("How much have you invested? ")
    interest_rate = input("Expected interest rate (in decimals)? ")
    times_compounded = input("How many times is the interest compounded per year? ")
    years = input("How many years will you be investing? ")


    components = [principal, interest_rate, times_compounded, years]

    cal1 = Compound_Cal(principal, interest_rate, times_compounded, years)


def auto_cal():

    cal2 = Compound_Cal(100, .10, 1, 1)
















'''def calculate_int(item):

    amount = item.principal * (1 + item.interest_rate / item.compound_rate) ** (item.compound_rate * item.years)

    print("This is the compounded amount : $" + str(amount))


#print("This is the NONcompounded amount : $" + str(amount2))

calculate_int(cal1)
calculate_int(cal2)'''

