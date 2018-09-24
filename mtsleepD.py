#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sandwich
# @Date:   2018-09-17 16:32:29
# @Last Modified by:   sandwich
# @Last Modified time: 2018-09-17 16:49:20

import threading
from time import sleep, ctime

class ThreadFunc:
	def __init__(self, func, args, name=''):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		"""将类交给Thread时， 会自行调用该方法"""
		self.func(*self.args)

def loop(nloop, nsec):
	print('start loop', nloop, 'at:', ctime())
	sleep(nsec)
	print('loop', nloop, 'done at:', ctime())


if __name__ == '__main__':
	print('start at:', ctime())
	loops = [4, 2]
	threads = []

	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(
			target=ThreadFunc(loop, (i, loops[i]), loop.__name__))	# 执行__call__()所以不再需要传递args参数
		threads.append(t)

	for i in nloops:
		threads[i].start()			# 开始线程

	for i in nloops:
		threads[i].join()		# 等待所有的线程结束

	print('all done at:', ctime())