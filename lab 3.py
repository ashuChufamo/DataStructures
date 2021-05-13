class Node:
      def __init__(self,data):
            self.data=data
            self.next=None

      
class CLinkedList:
      def __init__(self):
            self.head=None

      def listprint(self):
            printval=self.head
            while printval:
                  print (printval.data)
                  printval=printval.next
                  if printval==self.head:
                        break
      def prepend (self,data):
            NewNode= Node(data)
            cur= self.head
            NewNode.next=self.head
            if not self.head:
                  NewNode.next = NewNode   
            else:
                  while cur.next != self.head:
                        cur.next=NewNode
                  cur.next=NewNode
                  self.head=NewNode
      def append(self,data):
            if not self.head:
                  self.head=Node(data)
                  self.head.next= self.head
            else:
                  NewNode=Node(data)
                  cur=self.head
                  while cur.next != self.head:
                        cur=cur.next
                  cur.next=NewNode
        
list = CLinkedList()
list.append("one")
list.append("two")
list.listprint()
#list.append("three")
list.prepend("zero")
list.listprint()
