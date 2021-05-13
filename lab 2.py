class Node:
      def __init__(self,dataval=None):
            self.dataval=dataval
            self.nextval=None
            self.previosval=None

      
class DLinkedList:
      def __init__(self):
            self.headval=None

      def listprint(self):
            printval=self.headval
            while printval is not None:
                  print (printval.dataval)
                  printval=printval.nextval
                  
      def AtBegining (self,newdata):
            NewNode=Node(newdata)
            temp=self.headval
            self.headval.previosval=NewNode
            self.headval=NewNode
            NewNode.nextval=temp
            NewNode.previosval=None
      def remove(self,key):
            self.key=key
            counter=0
            temp=self.headval
            if 
            while self.key>counter:
                  temp=temp.nextval
                  counter+=1
            temp2=temp.previosval
            temp3=temp.nextval
            temp2.nextval=temp3
            temp3.previosval=temp2
      def Last(self,newdata):
            temp=self.headval
            NewNode=Node(newdata)
            while temp.nextval is not None:
                  temp=temp.nextval
             
            NewNode.previosval=temp
            temp.nextval=NewNode
            NewNode.nexttval=None
                   
list = DLinkedList()
list.headval=Node("one")
val2=Node("two")
val3=Node("three")

list.headval.nextval=val2
val2.nextval=val3
list.listprint()
print()
list.AtBegining("zero")
list.AtBegining("...negative numbers")
list.Last("four...")
list.listprint()
list.remove(5)
list.listprint()
