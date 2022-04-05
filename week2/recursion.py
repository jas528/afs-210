def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num,odd_sum):
    # Duplicate the loop1 function using recursion
    if (num >= 20):
        return odd_sum
    elif (num % 2) == 1:
        odd_sum += num
        # skip even numbers to reduce
        return loop1Rec (num+2,odd_sum)

    
def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
    if (num >= 20):
        return even_sum
    elif (num % 2) == 0:
        even_sum += num
        # skip odd numbers to reduce
        return loop2Rec (num+2,even_sum)
print(loop1Rec(1,0))
print(loop2Rec(0,0))