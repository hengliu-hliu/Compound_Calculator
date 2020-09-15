#Author: Henry
# Program to calculate compounded growth

# class containing components of each calcuation
class compound_cal:
    def __init__(self, principal, interest_rate, compound_rate, years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.compound_rate = compound_rate
        self.years = years

# calculates compounded value
# returns a string
def calculate(item):

    if item != False:

        principal = item.principal
        interest_rate = item.interest_rate
        compound_rate = item.compound_rate
        years = item.years

        amount = principal * (1 + interest_rate /
                              compound_rate) ** (compound_rate * years)
        #print("This is the compounded amount: $" + str(amount))

        str_amount = "This is the compounded amount: $" + str(amount)

        return str_amount

    else:
        #print("There is an issue with the input.")
        return "There is an issue with the input"

# checks if the input is value
# returns a list of values


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

# creates an instance of compound_cal from the input


def input_to_obj(input):
    if input != False:
        cal = compound_cal(input[0], input[1], input[2], input[3])
        return cal
    else:
        return False

# wrapper function
# evaluates, creates instances and runs calcuation


def run_cal(input):
    input_Ver = eval_input(input)
    Calculator1 = input_to_obj(input_Ver)
    result = calculate(Calculator1)

    return result


# Test Case
'''input1 = input_parameter()
print(input1)
input1_Ver = eval_input(input1)
print(input1_Ver)
Calculator1 = input_to_obj(input1_Ver)
calculate(Calculator1)
'''
