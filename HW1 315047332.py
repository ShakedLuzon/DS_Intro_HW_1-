#A
def my_func(x1,x2,x3):
    try:
        if type(x1) == float and type(x2) == float and type(x3) == float:
            return ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        else:
            return "Error: parameters should be float"
    except:
        return "Not a number - denominator equals zero"

print(my_func(3.,4.,3.))

#%%
#B
def convert(hours,minutes):
    if hours < 0 or minutes < 0 :
        return "Input error!"
    else:
        return hours*60*60 + minutes*60

print(convert(5, 7))