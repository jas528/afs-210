def push(self, data): 
       node = (data) 
       if self.top: 
           node.next = self.top 
           self.top = node                 
       else: 
           self.top = node 
       self.size += 1 

       #
       def pop(self): 
        if self.top: 
            data = self.top.data 
            self.size -= 1  
            if self.top.next: 
                self.top = self.top.next 
            else: 
                self.top = None 
            return data 
        else: 
            return None 
        
        def peek(self): 
         if self.top.next:
            return self.top.data 
         else: 
            return None 

        def enqueue(self, data): 
            self.items.insert(0, data) 
        self.size += 1

        def dequeue(self):
            data = self.items.pop()
        self.size -= 1
        return data    
        #
        def enqueue(self, data): 
            new_node = Node(data, None, None) 
        if self.head is None: 
            self.head = new_node 
            self.tail = self.head 
        else: 
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 

        self.count += 1 