#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sandwich
# @Date:   2018-09-17 18:52:49
# @Last Modified by:   sandwich
# @Last Modified time: 2018-09-17 19:11:56

from urllib.request import urlopen
from re import compile
from atexit import register
from threading import Thread
from time import ctime

def getRanking(AMZN, isbn, reg):
	page = urlopen('%s%s' % (AMZN, isbn))
	data = page.read()
	page.close()
	return reg.findall(data)[0]

if __name__ == '__main__':
	AMZN = r'http://amazon.com/dp/'
	reg = compile(r'#([\d,]+) in Books')
	ISBNs = {
		'0132269937' : 'Core Python Programming',
		'0132356139' : 'Python Web Development with Django',
		'0137143419' : 'Python Fundamentals',
	}
	# for isbn in ISBNs:
	# 	print(getRanking(AMZN, isbn, reg))
	# 	break
	print(getRanking(AMZN, '0132356139', reg))