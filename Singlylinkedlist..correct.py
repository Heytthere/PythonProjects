class node:
  def _init_(self,item):
    self.cv=item
    self.next=None
  def getNext(self):
    return self.next
#node_class
#linkList_class
class singlyLinkedList:
  def _init_(self):
    self.head=None
  def printList(self):
    print(self.head.cv)
    nextValue=self.head.next
    while not nextValue==None:
      print(nextValue.cv)
      nextValue=nextValue.next
  def append(self,item):
    if self.head==None:
      self.head=node(item)
    else:
      cp=self.head
      while cp.getNext()!=None:
        cp=cp.getNext()
      cp.next=node(item)
  def insertFirst(self,item):
    if self.head==None:
      self.head=node(item)
    else:
        cp=self.head
        self.head=node(item)
        self.head.next=cp
  def insertAt(self,pos,item):
    for i in range(1,pos):
      if i==1:
        cp=self.head
      else:
        cp=cp.getNext()
    n1=node(item)
    n1.next=cp.getNext()
    cp.next=n1
  
a=singlyLinkedList()
a.append(7)
a.append(23)
a.append(24)
a.append(77)
a.append(90)
a.insertAt(4,56)
a.printList()
