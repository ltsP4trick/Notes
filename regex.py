from re import *
# "^" make it starts from the beggining
# "$" its something about ending this thing


if match("^[A-Z][a-z]*$", "Vooooo"): #How many times you want
    print("yes1")
if match("^[A-Z][a-z]*$", "V"): 
    print("yes2")



if match("^[A-Z][a-z]?[A-Z]$", "VO"): #secound one is optional
    print("yes3")

if match("^[A-Z]{2,5}$","AAB"): #min 2 max 5
    print("yes4")


#also + means that it need to happen at least once

