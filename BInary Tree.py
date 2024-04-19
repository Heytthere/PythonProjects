
#Binary Tree Program.
class BinaryTree:
    def __init__(self):
        self.list1=[]
    def insert(self,item):
        self.list1.append(item)
    def isempty(self):
        if len(self.list1)==0:
            return True
        else:
            return False
    def leftchild(self,left):
        return self.list1[left*2-1]
    def rightchild(self,right=0):
        return self.list1[right*2]
    def preordertraversal(self,n=0):
        n+=1
        if not(len(self.list1)>=n):
            return 
        print(self.list1[n-1])
        self.preordertraversal(2*n-1)
        self.preordertraversal(2*n)
    def inordertraversal(self,p=0):
        p+=1
        if not(len(self.list1)>=p):
            return 
        self.inordertraversal(p*2-1)
        print(self.list1[p-1])
        self.inordertraversal(p*2)
    def postordertraversal(self,r=0):
        r+=1
        if not (len(self.list1)>=r):
            return 
        self.postordertraversal(r*2-1)
        self.postordertraversal(r*2)
        print(self.list1[r-1])
b=BinaryTree()
a=int(input("Enter Your Total Elements for Binary Tree List:"))
print()
for i in range(a):
    item=int(input("Please enter the %d element of Binary Tree list:"%i))
    b.insert(item)
print("\nYour Binary Tree List is:",b.list1)
print()
print("Here are 7 Choices to Apply in Binary Tree:")
print("Enter 1 for check if Binary Tree list is Empty or not..")
print("Enter 2 for Find Left child of Root node of Binary Tree.")
print("Enter 3 for Find Right child of Root node of Binary Tree.")
print("Enter 4 for print Preorder Traversal of Binary Tree.")
print("Enter 5 for print Inorder Traversal of Binary Tree.")
print("Enter 6 for print Postorder Traversal of Binary Tree.")
print("Enter 8 for Exit from program..")
print()
while True:
    s=int(input("Which Function do you want to Perform?"))
    if s==1:
        print(b.isempty())
    elif s==2:
        left=int(input("Please enter Root node whose left child you want to find:"))
        print("Left Child of root node is:",b.leftchild(left))
    elif s==3:
        right=int(input("Please enter Root node whose Right child you want to find:"))
        print("Right Child of root node is:",b.rightchild(right))
    elif s==4:
        b.preordertraversal()
    elif s==5:
        b.inordertraversal()
    elif s==6:
        b.postordertraversal()
    elif s==7:
        print("Thanks for Visiting..")
        break
    else:
        print("Please Select Valid Option..")
