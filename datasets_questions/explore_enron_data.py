#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print enron_data
#print len(enron_data)
nPOI = 0
nSalary = 0
nEmail = 0
for person, features_dict in enron_data.items():
	for key, value in features_dict.items():
		if key == 'poi' and value == True:
			nPOI += 1
		# How many folks have a quantified salary? Known email address?
		elif key == 'salary' and value != 'NaN':
			nSalary += 1
		elif key == 'email_address' and value != 'NaN':
			nEmail += 1


print 'POIs:', nPOI

print 'Total value of the stock belonging to James Prentice:', enron_data['PRENTICE JAMES']['total_stock_value']

print 'email messages from Wesley Colwell to persons of interest:', enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print 'value of stock options exercised by Jeffrey Skilling:', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

#print 'value of stock options exercised by Kenneth Lay:', enron_data['LAY KENNETH L']

print 'number valid salaries:', nSalary
print 'number valid email addresses:', nEmail
