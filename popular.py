from numpy import *
from matplotlib import pyplot as plt

def nextYearPopulation(x):
    y = r * x / (1 - x)
    
    return y


print("Population of rabbits")
r = float(input("birth rate: "))

x = float(input("population this year (0 is minumum and 1 is maximum possible population): "))

l = int(input("How many times should we literate?: "))
for z in range(l):
    x = nextYearPopulation(x)
    print("after this literation x equalts: ",x)