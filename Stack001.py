class stack:
    def __init__(self,length):
        self.li=[]
        self.size=length
    def push(self,item):
            self.li.append(item)
    def pop(self):
        self.li.pop()
    def peek(self):
        return self.li[-1]
    def stacksize(self):
        return len(self.li)
    def is_empty(self):
        if len(self.li)==0:
            return True
        else:  
            return False
    def is_full(self):
        if len(self.li)==self.size:
            return True
        else:
            return False
s=stack(10)
print(s.is_empty())
s.push(12)
s.push(32)
s.push(121)
s.push(45)
s.push(25)
print(s.is_empty())
print(s.peek())
s.pop()
#print(s.li)
print(s.is_full())
s.push(22)
s.push(55)
s.push(45)
s.push(550)
#s.push(599)
#s.push(100)
print(s.li)
print(s.stacksize())
#print(s.is_full())
