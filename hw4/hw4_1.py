import pandas
import statistics

data_set=pandas.read_csv('adult.csv')
data_age = data_set.iloc[:,0]
data_list=[]
for data in data_age:
    data_list.append(data)

data_list.sort()

print 'The MIN value is ', min(data_list)
print 'The MAX value is', max(data_age)
print 'The sum is',sum(data_age)
print 'Number of Elements',len(data_age)
print 'The Median is ', statistics.median(data_age)
data_age_mean = float(sum(data_age))/float(len(data_age))
print 'The mean is ', data_age_mean

data_det_var = sum([(number - data_age_mean)**2 for number in data_age]) / (len(data_age)-1)
data_age_MAD = [abs(number - data_age_mean) for number in data_age]
data_age_MAD.sort()

print 'The MAD is ', statistics.median(data_age_MAD)

print 'The variance is ', data_det_var

print 'Standard Daiation',data_det_var**0.5
