import random

def shuffleList(nlist):

    if len(nlist)<2:
        return nlist;
    else: 
        temp =  []
        while  (len(nlist))>=1:
            lastPos=len(nlist)-1
            firstPos=0
            randPos = random.randint(firstPos, lastPos)
            newlist=nlist[randPos]
            del nlist[randPos]
            temp.append (newlist)
    nlist=temp
    return nlist

myList= [7,20,26,31,40,51,55,63,74,81]
#random 
# #not sure which one it is
#list1= [7,20,26,31,40,51,55,63,74,81]
#print(shuffleList(list1,))
#list2= [7,20,26,31,40,51,55,63,74,81]
#print(shuffleList(list2,))

print(myList)
print(shuffleList(myList))

#ITS o(n) because of how manywe have its going to take 5 numbers how long 5 numbers will take direct cause time 
#If eat 5 jelly beans i will have 5 less jelly beans