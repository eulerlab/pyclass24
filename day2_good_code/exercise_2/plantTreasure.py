#!/usr/bin/python

import os
import random
from faker import Faker
import numpy as np

def init_treasure(treasure_path):
	# print(treasure_path)
	f = open(treasure_path,'a')
	q1 = 'Q1:\nProduct A and product B cost together 110 Euro, and A is 100 Euro more expensive than B.\nHow much does B cost?\n'
	q2 = 'Q2:\nIf you were to divide a gigantic research funding among vision, auditory, olfaction, gustation and haptic science, how many percent of it would you give to vision?'
	f.write(q1)
	f.write(q2)
	f.close()

def main():

	if os.path.exists("./startFolder/"):
		cmd = 'rm -r ./startFolder'
		os.system(cmd)
		print('removed existing folder')

	os.mkdir("startFolder")
	os.chdir("./startFolder/")

	# decide #subfolder and which subfolder has treasure
	np.random.seed(71)
	numFolders = random.randint(50,100)
	whereTreasure = random.randint(0,numFolders)

	# create folders with unique first names
	fake = Faker()
	names = [fake.unique.first_name() for i in range(numFolders)]

	# add treasure.txt file
	for i in range(numFolders):
		os.mkdir(names[i])
		if i == whereTreasure:
			cmd = "touch ./"+names[i]+"/treasure.txt"
			os.system(cmd)

			# initialize the content of the treasure.txt
			treasureWhere = os.getcwd()+'/'+names[i]+"/treasure.txt"
			init_treasure(treasureWhere)
		
if __name__ == "__main__":
	main()