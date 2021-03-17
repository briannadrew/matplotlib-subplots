# matplotlib.py

# Brianna Drew
# March 16, 2021
# ID: #0622446
# Lab #8

# import required libraries and modules
import numpy as np
import matplotlib.pyplot as plot
from pydataset import data

# import iris dataset
iris = data('iris')

# create scatter plot comparing sepal length to sepal width
plot.subplot(223)
plot.scatter(iris['Sepal.Length'], iris['Sepal.Width'], marker='x', c='green')
plot.title('Brianna Drew - #0622446')
plot.xlabel('Sepal Length')
plot.ylabel('Sepal Width')

# create scatter plot comparing petal length to petal width
plot.subplot(224)
plot.scatter(iris['Petal.Length'], iris['Petal.Width'], marker='x', c='magenta')
plot.title('Brianna Drew - #0622446')
plot.xlabel('Petal Length')
plot.ylabel('Petal Width')

# create pie chart
plot.subplot(221)
iris['Species'].value_counts().plot.pie(explode=[0.1,0.1,0.1],autopct='%1.1f%%',shadow=True)
plot.title('Brianna Drew - #0622446')
plot.ylabel('')

# create violin chart
plot.subplot(222)
plot.violinplot(iris.iloc[:,0:4])
plot.title('Brianna Drew - #0622446')
plot.xticks(np.arange(5), ['','Sepal Length','Sepal Width','Petal Length','Petal Width'])
plot.show()