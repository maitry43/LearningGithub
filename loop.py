x = 3
for i in range(1,x+1):
	for j in range(x,0,-1):
		if j>i:
			print(" ",end="")
		else:
			if i%2==0:
				print('!',end=""),
			else:
				print('#',end=""),
	print("\n")
