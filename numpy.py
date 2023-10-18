#1
import numpy as np
print("NumPy version:", np.__version__)

#2
ar = np.arange(10)
print("1D Array:", ar)

#3
iris = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = np.genfromtxt(iris, delimiter=',', names=column_names, dtype=None, encoding=None)

#4
i=0
while i < len(df['petal_width']):
    if df['petal_width'][i] >= 1:
        print('''The position of the first occurrence of a value greater than 1.0 in 
        petalwidth 4th column of iris dataset is at position''', i)
        break
    else:
        i+=1

#5
np.random.seed(100)
a = np.random.uniform(1,50, 20)

print(a)

for i in range(len(a)):
    if a[i] > 30:
        a[i] = 30
        print(a[i])
    elif a[i] < 10:
        a[i] = 10
        print(a[i])
    else:
        print(a[i])
        continue
