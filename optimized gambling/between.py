import math

def whole_btwn(a,b):
    c = 0.0
    counter = 0
    #if((int(a) == float(a)) & (int(b) == float(b))):
        #c = abs(a-b) - 1
    #else :
        #c = abs(a-b)
   
    #return round(c)
    if a>b:
        c = math.ceil(b)
        while ((c>=b) & (c<=a)):
            c = c+1
            counter = counter + 1
    elif b>a:
        c = math.ceil(a)
        while ((c>=a) & (c<=b)):
            c = c+1
            counter = counter + 1
   
    return counter
