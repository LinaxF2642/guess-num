

import random

r = random.randint(1, 100)
while True:
	num = input('請猜一個數字:  ')
	num = int(num)
	if num == r:
		print('恭喜！你答對了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')