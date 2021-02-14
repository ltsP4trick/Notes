def gener(x):
    i = 0
    while i <= x:
        if i%2 == 0:
            yield i         #yield is like return but it doesn't end function
        i += 1

for a in gener(10):
    print(a)

