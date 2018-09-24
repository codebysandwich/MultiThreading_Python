#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sandwich
# @Date:   2018-09-17 16:13:15
# @Last Modified by:   sandwich
# @Last Modified time: 2018-09-17 16:25:34

# from threading import Thread
import threading
from onethr import loop0, loop1, ctime

if __name__ == '__main__':
	print('start at:', ctime())
	# Thread.start_new_thread(loop0, ())
	# Thread.start_new_thread(loop1, ())
	threads = []
	t = threading.Thread(target=loop0, args=())
	threads.append(t)
	t = threading.Thread(target=loop1, args=())
	threads.append(t)
	for thread in threads:
		thread.start() 
	for thread in threads:
		thread.join() 
	print('all done at:', ctime())