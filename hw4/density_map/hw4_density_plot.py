import matplotlib.pyplot as plt
import pandas
import numpy as np
from scipy.stats import kde


adult_csv = pandas.read_csv('../adult.csv')
adult_age=(adult_csv.iloc[:,0]-(adult_csv.iloc[:,0].mean()))/(adult_csv.iloc[:,0].max()-adult_csv.iloc[:,0].min())
adult_salary=(adult_csv.iloc[:,2]-(adult_csv.iloc[:,2].mean()))/(adult_csv.iloc[:,2].max()-adult_csv.iloc[:,2].min())

nbins=75

k = kde.gaussian_kde([adult_salary,adult_age])

xi, yi = np.mgrid[adult_salary.min():adult_salary.max():nbins*1j, adult_age.min():adult_age.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

# Make the plot
plt.pcolormesh(xi, yi, zi.reshape(xi.shape))

plt.savefig('density_plot.png')
plt.show()
