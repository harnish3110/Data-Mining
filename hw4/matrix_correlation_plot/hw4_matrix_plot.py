import matplotlib.pyplot as plt
import pandas

adult_csv = pandas.read_csv('../adult.csv')
b= adult_csv.iloc[:,0]
a=adult_csv.iloc[:,2]
c=adult_csv.iloc[:,4]
d=adult_csv.iloc[:,11]
e=adult_csv.iloc[:,12]

df = pandas.DataFrame({'Salary': a})
df['Age'] = b
df['Date'] = c
df['Gain'] = d
df['HPW'] = e
df.corr()

plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()

plt.savefig('matrix_plot.png')
plt.show()
