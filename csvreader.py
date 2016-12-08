#!/usr/bin/python

import csv

def main():
	d = DataProcess()
	with open('stocks.csv') as f:
		f_csv = csv.DictReader(f)
		for row in f_csv:
			d.processdata(row['Close'])
	d.result() 
	

class DataProcess(object):
	def __init__(self):
		self.total = 0
		self.count = 0
	def processdata(self, data):
		self.total += float(data)
		self.count += 1
	def result(self):
		print (self.total/self.count) #print avg close

if __name__ == "__main__": main()
	
