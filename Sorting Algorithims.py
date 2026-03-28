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

for i in range(len(N) -1):
    for j in range(len(N) -1):
        if N[j] > N[j+1]:
            tempo = N[j]
            N[j] = N[j+1] #where are you storing(index) = what are you storing
            N[j+1] = tempo
print(N)