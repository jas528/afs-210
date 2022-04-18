class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        
        mult = 1 
        hv = 0 
        for ch in key: 
            hv += mult * ord(ch) 
            mult += 1 
        return hv % self.size 
    def rehash(self,key):
        # Insert your secondary hashing function code
        
        mult = 2 
        hv = 0 
        for ch in key: 
            hv += mult * ord(ch) 
            mult += 1 
        return hv % self.size 
    

    def put(self,key,data):
       hashvalue =self.hashfunction(key) 
       if self.data[hashvalue]==None:
           self.slots[hashvalue]=key
           self.data[hashvalue]=data
       else:
            if(self.slots[hashvalue]==key):
                self.data[hashvalue]=data
            else:
                hashvalue=self.rehash(key)
                if self.data[hashvalue]==None:
                    self.slots[hashvalue]=key
                    self.data[hashvalue]=data
                else:
                    return None
        # Insert your code here to store key and data 
        
    def get(self,key):
        hashValue=self.hashfunction(key)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue]is key:
                return self.data[hashValue]


        # Insert your code here to get data by key
        pass
    def __getitem__ (self,key):
        return self.get(key)
        
    def __setitem__ (self,key,data):
        self.put(key,data)
        

H = HashTable()
H[69] = 'A'
# Store remaining input data
H[66]='B'
H[80]='C'
H[35]='D'
H[18]='E'
H[52]='F'
H[89]='G'
H[70]='H'
H[12]='I'

# print the slot values
print (H.slots)
print(H.data)
print(H[52])

# print the data values

# print the value for key 52

