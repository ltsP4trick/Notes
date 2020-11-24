# [venv](https://docs.python.org/3/tutorial/venv.html)
virtualenv <insert-name> #or python -m venv <insert-name>
source <insert-name>/bin/activate

# end:
deactivate

# deleting folder will remove virtual environment (you need sudo)

# Strings:

print("this is \n in next line")

print(f'hello, {first} {last}')
print('hello, {} {}'.format(first,last))                                   # hello, patrick nowak
print('hello, {0} {1}'.format(first,last))                                 # hello, patrick nowak
print('hello, {0} {1}, its lovely to see you {0}'.format(first,last))     # hello, patrick nowak, its lovely to see you patrick

# ** to the power of

5 ** 3 == 125

from datetime import datetime

print(datetime.today().weekday())

print("what number squared gives 25?")
x = input("answer is: ")
if(int(x) == 5 or int(x) == -5):
    print("good job")
else:
    print("not really") 


print("what number squared gives 25?")
y = input("answer is: ")
if int(y) in(5, -5):   
    print("good job")
else:
    print("not really")

a = [0,1,2,3,4,5,6,7,8,9]
a[-1] #last char
a[:-1] #from the beginning up to last one
a[::-1] #reversed order