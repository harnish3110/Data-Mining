import matplotlib.pyplot as plt
import pandas
import numpy as np


adult_csv = pandas.read_csv('../adult.csv')

adult_age=(adult_csv.iloc[:,0]-(adult_csv.iloc[:,0].mean()))/(adult_csv.iloc[:,0].max()-adult_csv.iloc[:,0].min())
adult_salary=(adult_csv.iloc[:,2]-(adult_csv.iloc[:,2].mean()))/(adult_csv.iloc[:,2].max()-adult_csv.iloc[:,2].min())

colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(adult_age, adult_salary, s=area, c=colors, alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.savefig('scatter_plot.png')
plt.show()
