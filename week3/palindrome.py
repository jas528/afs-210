from dataclasses import dataclass


class Queue:
    def __init__(self): 
        self.items = []
#
    def isEmpty(self):
        return self.items ==[]

    def enqueue(self, data): 
        self.items.insert(0, data)
    
    def dequeue(self):
        return self.items.pop()

    def peek(self): 
         return self.items[-1]   
    
    def size(self): 
         return len(self.items)
    
class Stack:

    def __init__(self): 
        self.items = []   
    
    def isEmpty(self):
        return self.items ==[]

    def push(self, data): 
       self.items.append (data)
    
    def pop(self): 
       return self.items.pop() 
      
    def peek(self): 
       return self.items[-1]
      
    def size(self): 
       return len(self.items) 
       
def isPalindrome(str):
    strStack = Stack() 
    strQueue = Queue()

    for element in str:
        strStack.push(element)    
        strQueue.enqueue(element)
    
    for i in range(int(len(str)/2)):
       
        if (strStack.pop() != strQueue.dequeue()):
            return False
        else:
            return True
print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))

    
        
        

        
        

        
        