def exponent(num,exponent):
    # with built in function
    # return num**exponent
    result=1
    # for i in range(1,exponent+1):
    #     result=result*num
    # return result
    
    # using while loop
    i=1
    while i<=exponent:
        result*=num
        i+=1
    return result

print(exponent(6,2))

