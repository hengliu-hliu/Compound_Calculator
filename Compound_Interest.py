#Author: Henry
#Program to calculate compounded growth
import Cal_obj



def input_cal_int(item):

    principal = item.Cal_obj.principal
    interest_rate = item.Cal_obj.interest_rate
    compound_rate = item.Cal_obj.compound_rate
    years = item.Cal_obj.years

    amount = principal * (1 + interest_rate / compound_rate) ** (compound_rate * years)

    return amount

    print("This is the compounded amount : $" + str(amount))


#print("This is the NONcompounded amount : $" + str(amount2))

calculate_int(cal2)
