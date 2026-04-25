#Sorting algorithims
#===================


#Selection sort
#---------------
N = [10,999,25,5,15,2,6,8,9,11]
 
for o in range(len(N)):
    Sml = N[o]
    position = o
    for i in range(o + 1,len(N)):
        if N[i] < Sml:
            Sml = N[i]
            position = i
    temp = N[o]
    N[o] = Sml 
    N[position] = temp
print(N)


#Bubble sorting algorithim 
#-------------------------
N = [999,10,25,5,15,2,6,8,9,11]
for i in range(len(N)):
    for j in range(len(N) -1 - i) :
        if N[j] > N[j+1]:
            tempo = N[j]
            N[j] = N[j+1] #where are you storing(index) = what are you storing
            N[j+1] = tempo
print(N)

#Insertion Sort
#-------------- 
N = [999,10,25,5,15,2,6,8,9,11]
for i in range(1,len(N)):
    key = N[i]
    j  = i - 1
    while j >= 0 and key < N[j]:
        N[j + 1] = N[j]
        j  = j - 1 
    N[j + 1] = key
print(N)


#Merge sort
#----------
N = [999,10,25,5,15,2,6,8,9,11]
def mergeSort(N,firstI,lastI):
    if firstI < lastI:
        mid = (firstI + lastI) // 2 
        mergeSort(N,firstI,mid)
        mergeSort(N,mid + 1,lastI)
        merge(N,firstI,mid,lastI)
        
    
def merge(N,firstI,mid,lastI):
    result = []
    i1 = firstI
    i2 = mid + 1
    
    while i1 <= mid and i2 <=lastI:
        if N[i1] < N[i2]:
            result.append(N[i1])
            i1 = i1 + 1
        else:
            result.append(N[i2])
            i2 = i2 + 1

    while i1 <= mid:
        result.append(N[i1])
        i1 = i1 + 1 
    while i2 <= lastI:
        result.append(N[i2])
        i2 = i2 + 1
    
    for i in range(len(result)):
        N[firstI+i] = result[i]

mergeSort(N,0,len(N) -1)

print(N)









