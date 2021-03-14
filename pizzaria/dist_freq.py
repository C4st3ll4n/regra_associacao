from numpy import genfromtxt
import matplotlib.pyplot as plt

dataValorTotal = genfromtxt('vt.csv')
#histValorTotal = plt.hist(dataValorTotal)

dataTempo = genfromtxt('tempo.csv')
histTempo = plt.hist(dataTempo, bins=4)

plt.show()
