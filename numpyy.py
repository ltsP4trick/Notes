import numpy as np

a = np.array([7,4,3,8])
b = np.array([1,2,3,4])

np.arange(10, 30, 5) #add 5 to first number till you get second one

print(np.mean(a))  #arithmetic mean (mediana)
print(np.std(b)) #idk what it is
a.shape
a = np.linspace(2, 5, 10) # 2 + (5-3)/10 ## in 

a[0] #first number in array
a <3 #elements smaller that 3

print(np.append(b,[1,2,3,4],axis=0))     #put something (where, [what], which axis)     #[what] can be code too 
print(np.insert(a,0,b))     # add something at the end
print(np.sort(a))


np.newaxis(a)
np.reshape(a,)

np.linspace()