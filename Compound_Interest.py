#Author: Henry
# Program to calculate compounded growth

# Compound interest Calculator and components
class compound_cal:
    def __init__(self, principal, interest_rate, compound_rate, years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.compound_rate = compound_rate
        self.years = years


def calculate(item):

    principal = item.principal
    interest_rate = item.interest_rate
    compound_rate = item.compound_rate
    years = item.years

    amount = principal * (1 + interest_rate /
                          compound_rate) ** (compound_rate * years)
    print("This is the compounded amount : $" + str(amount))

    return amount

def input_parameter():

    principal = input("How much have you invested? ")
    interest_rate = input("Expected interest rate (in decimals)? ")
    compound_rate = input(
        "How many times is the interest compounded per year?")
    years = input("How many years will you be investing? ")

    input_num = (principal, interest_rate, compound_rate, years)

    return input_num


def eval_input(input):
    output_list = []

    for value in input:
        try:
            output_list.append(float(value))
        except ValueError as e:
            print("The input \'" + value + "\' isn't recognized")
            return False

    if len(output_list) == 4:
        return output_list


def input_to_obj(input):
    cal = compound_cal(input[0], input[1], input[2], input[3])

    return cal

  #  ***********************************


input1 = input_parameter()
print(input1)
input1_Ver = eval_input(input1)
print(input1_Ver)
Calculator1 = input_to_obj(input1_Ver)
# print(Calculator1)
calculate(Calculator1)
