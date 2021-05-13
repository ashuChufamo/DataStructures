class node :
      def __init__(self,data=None):
            self.data=data
            self.next=None

class SLL:
      def __init__ (self):
            self.head=None

      def append(self,value):
            new_value=node(value)
            current_val=self.head
            while current_val.next != None:
                  current_val=current_val.next
            current_val.next=value

      def printall(self):
            List=[]
            current_val=self.head
            while current_val != None:
                  current_val=current_val.next
                  List.append(current_val)
            return List


test=SLL()
test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
#return all values
#print(test.printall())
