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

print proportion_survivors

