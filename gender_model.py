import csv as csv
from pylab import *

test_file_object = csv.reader(open('./titanic-data/test.csv', 'rb'))
header = test_file_object.next() # skip header line

prediction_file_object = csv.writer(open('genderbasedmodel.csv', 'wb'))

prediction_file_object.writerow(['PassengerId', 'Survived'])
for row in test_file_object:
    if row[3] == 'female': # if female, predict 1
        prediction_file_object.writerow([row[0], '1'])
    else: # if male, predict 0
        prediction_file_object.writerow([row[0], '0'])


