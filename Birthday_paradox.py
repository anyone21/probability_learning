'''
This code use the Monte-carlo simulation to get a curve of 2 person having same day birthday for variable range of people in the 
group.
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

from random import randint
from datetime import datetime,timedelta

def random_birthdays(number_of_people):
  '''
  since birthdays are only the dates so we return a non dulplicate list of birtday dates.
  '''
	first_day_of_year = datetime(2019,1,1)
	return [first_day_of_year + timedelta(days=randint(0, 365))for _ in range(number_of_people)]

def determine_probability(number_of_people,run_amount = 1000):
  '''
  use the Monte-Carlo simulation for the 'number_of_people' and return the respective probability
  '''
	dups_found = 0
	for _ in range(run_amount):
		birthdays = random_birthdays(number_of_people)
		duplicates = set(x for x in birthdays if birthdays.count(x)>1)
		if(len(duplicates)>=1):
			dups_found += 1
	return dups_found/run_amount

if __name__ == "__main__":
	x  = [people for people in range(1,61)] # list of people in a group like[1,2,3...,60]
	y = []  # list contain the respective probabilites of the group
	for people in range(1,61):
		y.append(determine_probability(people))
	plt.plot(x,y)
	plt.show()
#Note : this simulation take few seconds to output the result
