import matplotlib.pyplot as plt
import pandas

adult_csv = pandas.read_csv('../adult.csv')
adult_age= adult_csv.iloc[:,0]


_ = plt.hist(adult_age, facecolor='blue')
plt.savefig('histogram.png')
plt.show()


