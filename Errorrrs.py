liczba = 0
try:
    print(5/liczba)
except ZeroDivisionError:
    print("nie dziel przez zero")
except NameError:
    print("")
finally:
    "yay"