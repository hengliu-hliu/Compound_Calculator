# Check if Str is number
def is_str_float(str):
    if str.isdecimal():
        return True

    else:
        print("The input " + str + " is not a number")
        return False


# converts str to float
def float_convert(str):
    temp = float(str)
    return temp



# converts items in list from str to float
# uses is_str_float and float_conert
def float_list(check):

    for atr in check.items():
        if is_str_float(atr):
            check.atr = float_convert(atr)
        else:
            print("There is an issue with the inputs.")
            quit()

'''for counter, item in enumerate (check):
        if is_str_float(item):
            check[counter] = float_convert(item)
        else:
            print("There is an issue with the inputs.")
            quit()'''






#test functions
#print(is_str_float("40"))
#print(is_str_float("h"))

