# Strings:
first = "Patryk"
last = "Nog"
print("this is \n in next line")
print(f'hello, {first} {last}')
print('hello, {} {}'.format(first,last))                                   # hello, patrick nowak
print('hello, {0} {1}'.format(first,last))                                 # hello, patrick nowak
print('hello, {0} {1}, its lovely to see you {0}'.format(first,last))     # hello, patrick nowak, its lovely to see you patrick

# y in (5,-5)
y=int(input("what is 25 squared?: " + "\n"))
if y in(5, -5):   
    print("good job")
else:
    print("not really")


# Chars, formatting
a = [0,1,2,3,4,5,6,7,8,9]
a[-1] #last char
a[:-1] #from the beginning up to last one
a[::-1] #reversed order

# 5 * 5 * 5
5 ** 3