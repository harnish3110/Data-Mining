import matplotlib.pyplot as plt
import pandas


adult_csv = pandas.read_csv('../adult.csv')
adult_age=(adult_csv.iloc[:,0]-(adult_csv.iloc[:,0].mean()))/(adult_csv.iloc[:,0].max()-adult_csv.iloc[:,0].min())

_=plt.boxplot(adult_age)
plt.savefig('box_plot.png')
plt.show()





