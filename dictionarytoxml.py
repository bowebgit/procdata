#!/usr/bin/python

from xml.etree.ElementTree import (Element, tostring)


def dict_to_xml(tag, d):
	#turn data dictionary into xml document
	elem = Element(tag)
	for key, val in d.items():
		child = Element(key)
		child.text = str(val)
		elem.append(child)
	return elem
	
s = {'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
print(tostring(e))

# output: b '<stock><price>490.1</price><shares>100</shares><name>GOOG</name></stock>'