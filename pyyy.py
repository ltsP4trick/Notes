"""
# run virtual env:
    python -m venv <insert-name>            # virtualenv <insert-name>
    source <inserted-name>/bin/activate

#to exit:
    deactivate
"""
# Strings:
first = "Patryk"
last = "Nog"
print("this is \n in next line")
print(f'hello, {first} {last}')
print('hello, {} {}'.format(first,last))                                   # hello, patrick nowak
print('hello, {0} {1}'.format(first,last))                                 # hello, patrick nowak
print('hello, {0} {1}, its lovely to see you {0}'.format(first,last))     # hello, patrick nowak, its lovely to see you patrick

# ** to the power of

5 ** 3 == 125

from datetime import datetime

print(datetime.today().weekday())


y=int(input("what is 25 squared?: " + "\n"))
if int(y) in(5, -5):   
    print("good job")
else:
    print("not really")

a = [0,1,2,3,4,5,6,7,8,9]
a[-1] #last char
a[:-1] #from the beginning up to last one
a[::-1] #reversed order

liczba = 0
try:
    print(5/liczba)
except ZeroDivisionError:
    print("nie dziel przez zero")
except NameError:
    print("")
finally:
    "yay"
