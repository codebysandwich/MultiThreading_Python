#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sandwich
# @Date:   2018-09-17 16:08:55
# @Last Modified by:   sandwich
# @Last Modified time: 2018-09-19 10:09:46

from time import sleep, ctime

def loop0():
	print('start loop 0 at:', ctime())
	sleep(4)
	print('loop 0 done at:', ctime())

def loop1():
	print('start loop 1 at:', ctime())
	sleep(2)
	print('loop 1 done at:', ctime())

if __name__ == '__main__':
	# print('start at:', ctime())
	# loop0()
	# loop1()
	# print('all done at:', ctime())

	nsum = 0
	for i in range(1999):
		fac = i % 2
		nsum += i* ((-1) ** fac)
		print(i* ((-1) ** fac))
	print(nsum)