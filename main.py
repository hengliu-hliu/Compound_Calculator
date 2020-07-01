import Cal_obj
import is_str_float


def main():


    principal = input("How much have you invested? ")
    interest_rate = input("Expected interest rate (in decimals)? ")
    times_compounded = input("How many times is the interest compounded per year? ")
    years = input("How many years will you be investing? ")

    components = [principal, interest_rate, times_compounded, years]



    cal1 = Cal_obj.Compound_Cal(principal, interest_rate, times_compounded, years)

 #   for each_item in Cal_obj.cal1.values():
 #       print(Cal_obj.cal1.each_item)

    print(Cal_obj.cal1.principal)
    print(Cal_obj.cal1.interest_rate)
    print(Cal_obj.cal1.years)

    print(Cal_obj.cal1.years + Cal_obj.cal1.interest_rate)

    print(is_str_float.is_str_float(Cal_obj.cal1.years))

    print(is_str_float.float_convert(Cal_obj.cal1.years) + is_str_float.float_convert(Cal_obj.cal1.years))


 #   is_str_float.float_list(components)
#    print(components)

#    is_str_float.float_list(cal1)

main()








