print('timer')

t = input('enter time to delay in sec(can be an expression):')
import time
t = eval(t) * 10

while True:
	for i in range(t+1)[::-1]:
		time.sleep(0.1)
		h = int(i/10 // 3600)
		m = int(i/10 % 3600) // 60
		s = int(i/10 % 60) // 1
		ms = i % 10
		print('\b'*10 + f'{h:02d}:{m:02d}:{s:02d}.{ms}',end='\r')

	# make an alert sound to notify end
	print('\n\a',end='\r')

import os
os.system('pause')