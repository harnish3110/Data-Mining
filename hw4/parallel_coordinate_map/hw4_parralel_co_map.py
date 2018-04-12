import matplotlib.pyplot as plt
import pandas
import seaborn as sns
# import numpy as np
# from scipy.stats import kde


adult_csv = pandas.read_csv('../adult.csv')
# adult_age=(adult_csv.iloc[:,0]-(adult_csv.iloc[:,0].mean()))/(adult_csv.iloc[:,0].max()-adult_csv.iloc[:,0].min())
# adult_salary=(adult_csv.iloc[:,2]-(adult_csv.iloc[:,2].mean()))/(adult_csv.iloc[:,2].max()-adult_csv.iloc[:,2].min())

adult_salary=adult_csv.iloc[:,2]
# adult_age= pandas.cut(adult_csv.iloc[:,0],[8,16,24,32,50])
adult_age = adult_csv.iloc[:,0]

data = sns.load_dataset('iris')

# Make the plot
pandas.plotting.parallel_coordinates(data, 'species', colormap=plt.get_cmap("Set2"))
plt.savefig('parallel_co_map.png')
plt.show()

