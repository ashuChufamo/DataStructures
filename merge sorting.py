def mergeSort(nList):
      if len(nList)>1:
            mid= len(nList)//2
            leftHalf=nList[:mid]
            rightHalf=nList[mid:]

            mergeSort(leftHalf)
            mergeSort(rightHalf)
            i=j=k=0

            while i < len(leftHalf) and j<len(rightHalf):
                  if leftHalf[i]<rightHalf[j]:
                        nList[k]=leftHalf[i]
                        i+=1
                  else:
                        nList[k]=rightHalf[j]
                        j+=1
                  k+=1
                  
            while i< len(leftHalf):
                  nList[k]=leftHalf[i]
                  i+=1
                  k+=1

            while j < len(rightHalf):
                  nList[k]=rightHalf[j]
                  j+=1
                  k+=1
#quick
#shell
nList=[14,46,43,27,57,41,45,21,70]
mergeSort(nList)
print(nList)
            
