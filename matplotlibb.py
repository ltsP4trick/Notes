import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

values = [65853514, 62984828]

names = ["Hillary Clinton", "Donald Trump"]

a=plt.bar(names,values)

plt.ylabel('1 is 10 milions')


a[1].set_color('r')
a[0].set_color('b')


plt.show()