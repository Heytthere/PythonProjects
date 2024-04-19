class Queue:
    def __init__(self,length):
        self.list=[]
        self.size=length
    def enqueue(self,item):
            self.list.append(item)
    def dequeue(self):
        self.list.pop(0)
    def peek(self):
        return self.list[0]
    def queuesize(self):
        return len(self.list)
    def is_empty(self):
        if len(self.list)==0:
            return True
        else:  
            return False
    def is_full(self):
        if len(self.list)==self.size:
            return True
        else:
            return False
q=Queue(20)

q.enqueue(12)
q.enqueue(24)
q.enqueue(55)
q.enqueue(40)
q.enqueue(54)
q.enqueue(34)
print(q.list)
q.dequeue()
print(q.list)
print(q.peek())
print(q.is_empty())
print(q.is_full())
print(q.queuesize())