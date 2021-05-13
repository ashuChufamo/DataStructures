#ASHENAFI CHUFAMO
class Node:
      def __init__(self,dataval=None):
            self.dataval=dataval
            self.nextval=None
      
class SLinkedList:
      def __init__(self):
            self.headval=None

      def listprint(self):
            printval=self.headval
            while printval is not None:
                  print (printval.dataval)
                  printval=printval.nextval
                  
      def AtBegining (self,newdata):
            NewNode=Node(newdata)            
            NewNode.nextval=self.headval
            self.headval=NewNode
            
      def InMiddle (self,position,newdata):            
             self.position=position
             NewNode=Node(newdata)
             counter=0
             temp=self.headval
             if self.position!=0:
                   self.position-=1           
                   temp=self.headval
                   while self.position!=counter and temp.nextval is not None:
                         temp=temp.nextval
                         counter+=1
                   temp2=temp.nextval                   
                   temp.nextval=NewNode
                   NewNode.nextval=temp1
             else:
                   self.AtBegining(newdata)#call the prepend method
                   
      def toDel (self,position):
             self.position=position
             counter=0
             temp=self.headval
             temp2=temp
             if self.position>1:
                   self.position-=1
                   while self.position > counter and temp.nextval is not None:
                         temp2=temp
                         temp=temp.nextval
                         counter+=1                 
                   temp2.nextval=temp.nextval                   
             else:
                   self.headval=temp.nextval#set the next to be the head value, which leaves the first head value to be null
      def lengthCounter(self):
            temp=self.headval
            counter=0
            while temp!=None:
                  counter+=1
                  temp=temp.nextval
            return counter
      def getIndex (self,datavalue):
            self.datavalue=datavalue
            temp=self.headval
            counter=0
            listLength=self.lengthCounter()
            while counter<listLength:
                  if temp.dataval==self.datavalue:
                        return counter
                  temp=temp.nextval
                  counter+=1
      def removeRedendent(self):
            listLength=self.lengthCounter()
            counter=0
            temp=self.headval
            temp2=self.headval
            temp2=temp2.nextval
            while counter <listLength:
                  counter2=0
                  while counter2 != listLength:
                        if temp2==None:
                              temp.nextval=None
                              p=counter2-listLength
                              counter2-=p  
                        elif   temp.dataval!=None and temp2.dataval!=None and temp.dataval==temp2.dataval:
                              listLength-=1
                              counter2+=1
                        else:
                              temp.nextval=temp2
                              p=counter2-listLength
                              counter2-=p
                        if temp2!=None:
                              temp2=temp2.nextval
                  counter+=1
                  if temp2!=None:
                        temp=temp.nextval
                        temp2=temp.nextval
      def anywhereRemover(self):
            #self.removeRedendent()
            temp=self.headval
            counter=0
            listLength=self.lengthCounter()
            temp2=temp.nextval
            while counter<listLength:
                   counter2=0
                   while counter2 != listLength:
                        if temp2==None:
                              temp.nextval=None
                              p=counter2-listLength
                              counter2-=p
                        elif temp.dataval==temp2.dataval:
                              index=self.getIndex(temp2.dataval)
                              self.toDel(index)
                        counter+=1
                        if temp2!=None:
                              temp2=temp2.nextval
                   counter+=1
                   if temp2!=None:
                        temp=temp.nextval
                        temp2=temp.nextval
                        
      def Last(self,newdata):
             temp=self.headval
             NewNode=Node(newdata)
             while temp.nextval is not None:
                   temp=temp.nextval
             temp.nextval=NewNode   
print("ashenafi chufamo")         
list = SLinkedList()
list.headval=Node("one")
val2=Node("two")
val3=Node("three")
val4=Node("four")

list.headval.nextval=val2
val2.nextval=val3
val3.nextval=val4
print("our initial values")

list.AtBegining("one")
list.AtBegining("zero")
list.AtBegining("one")

list.listprint()
print()

list.removeRedendent()
list.anywhereRemover()

print("our updated values")
list.listprint()


