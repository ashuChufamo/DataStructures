class Stack:
      def __init__(self):
            self.stack=[]

      def push(self,dataval):
            #if dataval not in self.stack:
            self.stack.append(dataval)
            #      return True
            #else:
              #    return False
      def pop(self):
            if len(self.stack)<=0:
                  return ("No element in the Stack")           
            else:
                  return self.stack.pop()
            
      def peek(self):
            return self.stack[0]
      
      def reverse(self):
            return self.stack[::-1]
      
AStack=Stack()
AStack.push("I")
AStack.push("F")
AStack.push("A")
AStack.push("N")
AStack.push("E")
AStack.push("H")
AStack.push("S")
AStack.push("A")

#print(AStack.remove())
print(AStack.reverse())
#i=AStack.pop()
#print(i)
#AStack.peek()
#print(AStack.peek())
#AStack.push("C")
#print(AStack.stack)
