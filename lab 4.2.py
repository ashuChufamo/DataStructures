class Queue:
      def __init__(self):
            self.queue=list()
      def add(self,dataval):
            if dataval not in self.queue:
                  self.queue.insert (0,dataval)
                  return True
            else:
                  return False
      def size(self):
            return len(self.queue)
      def remove(self):
            if len(self.queue)<=0:
                  return ("No elemoents in Queue!")
            else:
                  return self.queue.pop()
Que=Queue()
Que.add("A")
Que.add("B")
Que.add("C")
print(Que.remove())
print (Que.size())
