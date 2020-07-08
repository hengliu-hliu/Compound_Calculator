#Author: Henry
#Program to calculate compounded growth

# Compound interest Calculator and components
class compound_cal:
    def __init__(self, principal, interest_rate, compound_rate, years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.compound_rate = compound_rate
        self.years = years


# formula
def calculate(item):

    principal = item.principal
    interest_rate = item.interest_rate
    compound_rate = item.compound_rate
    years = item.years

    amount = principal * (1 + interest_rate / compound_rate) ** (compound_rate * years)

    return amount

    print("This is the compounded amount : $" + str(amount))


#print("This is the NONcompounded amount : $" + str(amount2))

def input_cal():

    principal = input("How much have you invested? ")
    interest_rate = input("Expected interest rate (in decimals)? ")
    compound_rate =  input("How many times is the interest compounded per year?")
    years = input("How many years will you be investing? ")

    input_num = (principal, interest_rate, compound_rate, years)

    return input_num



test = compound_cal(100,0.10,12,10)
print(calculate(test))

print(input_cal())
test3 = compound_cal(input_cal())
print(calucalate(test3))

'''
test2 = Compound_Cal (

    input("How much have you invested? "),
    input("Expected interest rate (in decimals)? "),
    input("How many times is the interest compounded per year?"),
    input("How many years will you be investing? ")
    )

print(test2)
'''
