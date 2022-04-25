
            
def binarySearch(alist,item):
    first = 0
    last = len(alist)-1

    while first <= last: #find the first item
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                last = midpoint -1

            else:
                first =midpoint + 1

    return False

list1=[7,20,26,31,40,51,55,63,74,81]
print(binarySearch(list1,31))
list2=[7,20,26,31,40,51,55,63,74,81]
print(binarySearch(list2,77))
list3=["Alpha","Beta","Delta","Epsilon","Gamma","Theta","Zeta"]
print(binarySearch(list3,"Delta"))
