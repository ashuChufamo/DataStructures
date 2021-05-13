#from array import *
#ashu=array('i',[1,2,3,4,5,6])
#for x in ashu:
  #    print (x)
#ashu.insert(1,3)
#for x in ashu:
  #    print (x)
#print (ashu[2])
#print(ashu.index[2])
#ashu[0]=4
#for x in ashu:
 #     print(x)

 
#class Node:
 #     def __init__(self,dataval=None):
 #           self.dataval=dataval
 #           self.nextval=None

#class SLinkedList:

  #    def __init__(self):
    #        self.headval=None
      #def listprint(self):
        #    printval=self.headval
          #  while printval is not None:
            #      print (printval.dataval)
              #    printval=printval.nextval
#list=SLinkedList()
#list.headval=Node("one")
#val2=Node ("two")
#val3=Node ("three")

#link first node to the second node
#list.headval.nextval=val2

#link second node to the third node
#val2.nextval=val3

#list.listprint()



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
             # printval=self.headval
             self.position=position
             NewNode=Node(newdata)
             temp1=None
             counter=0
             temp=self.headval
             if self.position!=0:
                   self.position-=1
           
                   temp=self.headval
                   while self.position!=counter and temp.nextval is not None:
                         temp=temp.nextval
                         counter+=1
                   temp1=temp.nextval
                   #temp.nextval.nextval=temp.nextval
                   temp.nextval=NewNode
                   NewNode.nextval=temp1
             else:
                   self.AtBegining(newdata)
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
                      
                   #temp1=temp.nextval
                   temp2.nextval=temp.nextval
                   #print(temp2.dataval)
                   #temp.nextval=temp1
                   #print(temp.dataval)
                   #temp.nextval.nextval=temp.nextval
                   #temp=temp1
                   #NewNode.nextval=temp1
             else:
                   self.headval=temp.nextval
      def Last(self,newdata):
             temp=self.headval
             NewNode=Node(newdata)
             while temp.nextval is not None:
                   temp=temp.nextval
             temp.nextval=NewNode  
             #NewNode.nextval=None
          
list = SLinkedList()
list.headval=Node("one")
val2=Node("two")
val3=Node("three")
val4=Node("four")


list.headval.nextval=val2
val2.nextval=val3
val3.nextval=val4
#list.listprint()
list.toDel(1)#not index, insert the value location, not 0 indexed, it is 1 indexed
#list.AtBegining("zero")
#list.InMiddle(1,"hey")
#list.Last ("five")
#list.Last ("six")
list.listprint()


