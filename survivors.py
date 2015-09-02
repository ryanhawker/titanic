import csv as csv
from pylab import *

csv_object = csv.reader(open('./titanic-data/train.csv', 'rb'))
header = csv_object.next() # skip header line

data = []
for row in csv_object: # read in rows from csv file into the data list
    data.append(row)

data = array(data) # convert to numpy array

number_passengers = size(data[:,1].astype(float))
number_survived = sum(data[:,1].astype(float))

proportion_survivors = number_survived / number_passengers

women_only = data[:,4] == "female" # finds all females from gender coloumn
men_only = data[:,4] != "female" # finds all males from gender coloumn

women_onboard = data[women_only,1].astype(float)
men_onboard = data[men_only,1].astype(float)

# proportions of women and men that survived
prop_women_survived = sum(women_onboard) / size(women_onboard)
prop_men_survived = sum(men_onboard) / size(men_onboard)

print 'Proportion of women who survived: %s' % prop_women_survived
print 'Proportion of men who survived: %s' % prop_men_survived

print 'Proportion of survivors: %s' % proportion_survivors

