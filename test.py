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

    print(len(output_list))
    if len(output_list) == 4:
        return output_list


print(eval_input(input_parameter()))
