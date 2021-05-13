#NAME:  ASHENAFI CHUFAMO
#ID: ATR/3774/10
#SECTION 1

def InsetionSort(theList):
    for iterator1 in range(1,len(theList)):#get the first index
        temporary =theList[iterator1]#backup as temporary
        iterator2=iterator1 #initialize second index from the first No.       
        while iterator2>0 and theList[iterator2-1]>temporary:#iterate till the end
            theList[iterator2]=theList[iterator2-1]#change the value
            iterator2-=1#iterate down
        theList[iterator2]=temporary#change the value of the second value to be the backup, temporary        
    return theList#give the result



def bubbleSort(theList):
    for iterator1 in range (0,len(theList)-1):#get the first No.
        for iterator2 in range (0,len(theList)-iterator1-1):#get the second No.
            if theList[iterator2]>theList[iterator2+1]:#check if the first No. is less 
                theList[iterator2],theList[iterator2+1] = theList[iterator2+1],theList[iterator2]#if so,swap the two numbers
    return(theList)#give the result



def selectionSort(theList):
    for iterator1 in range(len(theList)):#get first No. 
        minimumValue= iterator1 #Set it to be the min
        for iterator2 in range(iterator1+1, len(theList)): #get second No.
            if theList[minimumValue] > theList[iterator2]: #check if it is less than the min
                minimumValue = iterator2#change the min to be the second No.
        theList[iterator1], theList[minimumValue] = theList[minimumValue], theList[iterator1]#swap the first No. and the min
    return theList#give the result


print("The List [13,14,65,4,12,1,15,0,7]  by bubble sort will be...")
print(bubbleSort([13,14,65,4,12,1,15,0,7]))
print("The List [21,25,58,48,15,5,56,2,0,45,1] by insertion sort will be...")
print(InsetionSort([21,25,58,48,15,5,56,2,0,15,45,1]))
print("The List [12,15,48,92,59,36,15,2,8,96,15] by insertion sort will be...")
print(selectionSort([12,15,48,92,59,36,15,2,8,96,15]))

