position =0
def linearSearch(List,num):
      i=0
      while i< len(List):
            if List[i]==num:
                  globals()['position']=i
                  return True
            i+=1
      return False
List=[4,8,2,1,9,3]
if (linearSearch(List,3)):
      print("Number is at position",position,"::")
else:
      print("Number is not in the List!")
def binarySearch(List,num):
      i=0
      j=len(List)-1
      while i<=j:
            m=(i+j)//2
            if num==List[i]:
                  return i
            else:
                  if num>List[m]:
                        i=m+1
                  else:
                        j=m      
      return "not here"
print(binarySearch([4,8,2,1,9,3],1))
