from calendar import c
import time
import random
from tracemalloc import start

def quick_sort(a_list,start,end):

    if start>=end:
        return

    pivot = partitionStart(a_list,start,end)
    quick_sort(a_list,start, pivot-1)
    quick_sort(a_list, pivot+1, end)


def median(a,b,c):
    #returns the median of 3 numbers
    if(a-b) * (c-a)>=0:
        return a 
    elif (b-a)* (c-b)>=0:
        return b
    else: 
        return c


def partition(a_list,start,end):
    pivot = a_list [start]
    low =start + 1
    high = end

    while True:

        while low<=high and a_list[high]>=pivot:
             high = high -1

        while low <= high and a_list[low] <= pivot:
             low = low +1


        if low <= high:

            a_list[low], a_list[high]= a_list[high],a_list[low]
        
        else:
            break

    a_list[start], a_list[high]= a_list[high],a_list[start]
    return high     


def partitionMedianOf3(a_list,start,end):

    if (len(a_list)==0):
        middle =(len(a_list)//2)-1

    else:
        middle =len(a_list)//2

    pivot= median(a_list[start],a_list[end],a_list[middle])

    pivotIndex = a_list.index(pivot)

    a_list[start], a_list[pivotIndex]=a_list[pivotIndex], a_list[start]

    return partition(a_list,start,end)

def partitionRandom(a_list,start,end):
    #swap 1st element with random
    #call p function
    randomPivot = random.randrange(start,end)
    a_list[start], a_list[randomPivot]=a_list[randomPivot], a_list[start]
    return partition(a_list,start,end)

def partitionEnd(a_list,start,end):
    a_list[start], a_list[end]= a_list[end], a_list[start]
    return partition(a_list, start,end)

def partitionStart(a_list,start,end): 
    return partition(a_list, start,end)

print("Quick Sort:")
myList =[x for x in range (1000)]
random.shuffle(myList)
#mylist=
start_time =time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")