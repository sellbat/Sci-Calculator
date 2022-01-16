#from itertools import combinations, chain, permutations
#import numpy as np
#import math
#import pandas as pd
## Building Model
#from sklearn import linear_model

#n = int(input("Enter The Amount of objects in the List: "))
#print("Enter the values of the objects in the list")
#z = []
#p = []
#q = []
#for i in range(0,n):
#  x = float(input())
#  p.append(x)
#for i in range(0, len(p)):
##  j = math.exp(p[i])
 # q.append(j) #make exponential
#c = list(chain.from_iterable(list(combinations(q,i) for i in range(2,len(q)+1)))) #generating permutations of the values of the list
#results1 = []
#for x in c:
#  for n in range(len(x)):
#    results1.append((x[n])/(sum((x)))) #generating probabilities of choice based on the values
##print("Probability of choice based on the values are:", results1)
#results = np.array(results1)
#list2 = np.array(c, dtype=object)
#list1 = list(c)
#it = iter(results)
#list1 = [[next(it) for _ in sublist] for sublist in list1]
##list1 = np.array(list1, dtype=object)
#results = np.array(results, dtype=object)
#def geomean(xs):
#    return math.exp(math.fsum(math.log(x) for x in xs) / len(xs))
#for x in list1:
#  for n in range(len(x)):
#    l = math.log(x[n]/geomean(x))
#    z.append(l)
#independent = []
#f = []
#for i in range(len(c)):
#  for x in range(len(list2[i])):
#    for j in range(len(q)):
#      if list2[i][x] == q[j]:
#        independent.append(1-1/len(c[i]))
#      elif list2[i].count(q[j]) > 0 and list2[i][x] != q[j]:
#        independent.append(-1/len(c[i]))
#      else:
##        independent.append(0)
#x = np.reshape(independent, (len(z), n+1))
##print(x)
##y = np.array(z, dtype=object)
#regr = linear_model.LinearRegression()
#regr.fit(x, y)
#print(y)
#print(regr.coef_)
#data = pd.DataFrame(data=x)
#regr = linear_model.LinearRegression()
#model = regr.fit(x, y)
#print('Intercept:', model.intercept_)
#print('Coefficients:', model.coef_)