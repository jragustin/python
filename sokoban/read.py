'''
namomove na ung 'b' pero d pa namomove ung 'B'
'''





from tkinter import *
import copy 

f = open("puzzle.in", "r")

a = f.read().split("\n")
b = [[]]*10
listoflist = []
curr = 0

for z in range(0,len(a)):
	b[z] = a[z].split()
print(len(b))

for i in range(0,9):
	for j in range(0,9):
		# current[i] = init[i]
		if b[i][j] == "k" :
			horizontal = j
			vertical = i
			# print("vertical: ",i, "horizontal:", j)	
			# print(current[i][j])
		# print(b[i][j], end = " ")
	# print()	
#	print(b[x])

init = b[:]
prev = b[:]
current = b[:]
listoflist.append(copy.deepcopy(init))
curr+=1
# print(listoflist)
while True:
	# print("position: ",vertical, horizontal)	
	# print(current[vertical][horizontal])


	print("Previous                      Current")
	for i in range(0,9):
		for j in range(0,9):
			print(listoflist[curr-2][i][j], end = " ")
		print(" ", end = " ")
		for j in range(0,9):
			print(current[i][j], end = " ")
			# print(init[i][j], end = " ")
		print()

	print(curr)
	action = input("What to do: ")

	if (action == 'q'):
		break
	# MOVE UP
	elif action == 'w':

		if current[vertical-1][horizontal] == 'e':
			# prev = current
			current[vertical-1][horizontal]='k'
			current[vertical][horizontal]='e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical-1][horizontal]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical-1][horizontal]='k'
				current[vertical][horizontal]='e'

			vertical-=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1

		elif current[vertical-1][horizontal] == 's':
			# prev = current[:]
			current[vertical-1][horizontal]='k'
			current[vertical][horizontal]='e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical-1][horizontal]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical-1][horizontal]='k'
				current[vertical][horizontal]='e'

			vertical-=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1

		elif current[vertical-1][horizontal] == 'b':
			if current[vertical-2][horizontal] == 'e':
				current[vertical-2][horizontal] = 'b'
				current[vertical-1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='e'
				
				vertical-=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical-2][horizontal]=='s':
				current[vertical-2][horizontal] = 'B'
				current[vertical-1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='e'	

				vertical-=1
				listoflist.append(copy.deepcopy(current))
		
		elif current[vertical-1][horizontal] == 'B':
			print("hello","prev: ",listoflist[curr-2][vertical][horizontal])

			if current[vertical-2][horizontal] == 'e':
				current[vertical-2][horizontal] = 'b'
				current[vertical-1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='e'
				elif listoflist[curr-2][vertical][horizontal]=='B':
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='s'
				vertical-=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical-2][horizontal]=='s':
				current[vertical-2][horizontal] = 'B'
				current[vertical-1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='e'	
				elif listoflist[curr-2][vertical][horizontal]=='B': #previous
					current[vertical-1][horizontal]='k'
					current[vertical][horizontal]='s'
				vertical-=1
				listoflist.append(copy.deepcopy(current))		


	# MOVE LEFT
	elif action == 'a':
		if current[vertical][horizontal-1] == 'e':
			# prev = current[:]
			current[vertical][horizontal-1]='k'
			current[vertical][horizontal]='e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical][horizontal-1]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical][horizontal-1]='k'
				current[vertical][horizontal]='e'

			horizontal-=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1
		elif current[vertical][horizontal-1] == 's':
			# prev = current[:]
			current[vertical][horizontal-1] = 'k'
			current[vertical][horizontal] = 'e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical][horizontal-1]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical][horizontal-1]='k'
				current[vertical][horizontal]='e'

			horizontal-=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1
		elif current[vertical][horizontal-1] == 'b':
			if current[vertical][horizontal-2] == 'e':
				current[vertical][horizontal-2] = 'b'
				current[vertical][horizontal-1] = 'k'
				current[vertical][horizontal] = 'e'
				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='e'
				
				horizontal-=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical][horizontal-2]=='s':
				current[vertical][horizontal-2] = 'B'
				current[vertical][horizontal-1] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='e'

				horizontal-=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1

		elif current[vertical][horizontal-1] == 'B':
			if current[vertical][horizontal-2] == 'e':
				current[vertical][horizontal-2] = 'b'
				current[vertical][horizontal-1] = 'k'
				current[vertical][horizontal] = 'e'
				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='e'
				elif listoflist[curr-2][vertical][horizontal]=='B': #previous
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='s'

				horizontal-=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical][horizontal-2]=='s':
				current[vertical][horizontal-2] = 'B'
				current[vertical][horizontal-1] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='e'
				elif listoflist[curr-2][vertical][horizontal]=='B': #previous
					current[vertical][horizontal-1]='k'
					current[vertical][horizontal]='s'
				horizontal-=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
	# MOVE DOWN
	elif action == 's':
		if current[vertical+1][horizontal] == 'e':
			# prev = current[:]
			current[vertical+1][horizontal]='k'
			current[vertical][horizontal]='e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical+1][horizontal]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical+1][horizontal]='k'
				current[vertical][horizontal]='e'

			vertical+=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1
		elif current[vertical+1][horizontal] == 's':
			# prev = current[:]
			current[vertical+1][horizontal] = 'k'
			current[vertical][horizontal] = 'e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical+1][horizontal]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical+1][horizontal]='k'
				current[vertical][horizontal]='e'

			vertical+=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1
		elif current[vertical+1][horizontal] == 'b':
			if current[vertical+2][horizontal] == 'e':
				current[vertical+2][horizontal] = 'b'
				current[vertical+1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'
				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='e'
				
				vertical+=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical+2][horizontal]=='s':
				current[vertical+2][horizontal] = 'B'
				current[vertical+1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='e'	
									
				vertical+=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
		elif current[vertical+1][horizontal] == 'B':
			if current[vertical+2][horizontal] == 'e':
				current[vertical+2][horizontal] = 'b'
				current[vertical+1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'

				print("prev: ",listoflist[curr-2][vertical][horizontal])
				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr+2][vertical][horizontal]=='e':
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='e'
				elif listoflist[curr-2][vertical][horizontal]=='B':
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='s'
				vertical+=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical+2][horizontal]=='s':
				current[vertical+2][horizontal] = 'B'
				current[vertical+1][horizontal] = 'k'
				current[vertical][horizontal] = 'e'
				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr+2][vertical][horizontal]=='e':
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='e'	
				elif listoflist[curr-2][vertical][horizontal]=='B':
					current[vertical+1][horizontal]='k'
					current[vertical][horizontal]='s'
				vertical+=1
				listoflist.append(copy.deepcopy(current))


	# MOVE RIGHT
	elif action == 'd':
		if current[vertical][horizontal+1] == 'e':
			# prev = current[:]
			current[vertical][horizontal+1]='k'
			current[vertical][horizontal]='e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical][horizontal+1]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical][horizontal+1]='k'
				current[vertical][horizontal]='e'

			horizontal+=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1
		elif current[vertical][horizontal+1] == 's':
			# prev = current[:]
			current[vertical][horizontal+1] = 'k'
			current[vertical][horizontal] = 'e'
			if listoflist[curr-2][vertical][horizontal]=='s': #previous
				current[vertical][horizontal+1]='k'
				current[vertical][horizontal]='s'
			elif listoflist[curr-2][vertical][horizontal]=='e':
				current[vertical][horizontal+1]='k'
				current[vertical][horizontal]='e'

			horizontal+=1
			listoflist.append(copy.deepcopy(current))
			# listoflist.append(current[:])
			curr+=1
		elif current[vertical][horizontal+1] == 'b':
			if current[vertical][horizontal+2] == 'e':
				current[vertical][horizontal+2] = 'b'
				current[vertical][horizontal+1] = 'k'
				current[vertical][horizontal] = 'e'
				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='e'
				
				horizontal+=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical][horizontal+2]=='s':
				current[vertical][horizontal+2] = 'B'
				current[vertical][horizontal+1] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='e'


				horizontal+=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1

		elif current[vertical][horizontal+1] == 'B':
			if current[vertical][horizontal+2] == 'e':
				current[vertical][horizontal+2] = 'b'
				current[vertical][horizontal+1] = 'k'
				current[vertical][horizontal] = 'e'
				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='e'
				elif listoflist[curr-2][vertical][horizontal]=='B': #previous
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='s'
				
				horizontal+=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1
			elif current[vertical][horizontal+2]=='s':
				current[vertical][horizontal+2] = 'B'
				current[vertical][horizontal+1] = 'k'
				current[vertical][horizontal] = 'e'

				if listoflist[curr-2][vertical][horizontal]=='s': #previous
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='s'
				elif listoflist[curr-2][vertical][horizontal]=='e':
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='e'
				elif listoflist[curr-2][vertical][horizontal]=='B': #previous
					current[vertical][horizontal+1]='k'
					current[vertical][horizontal]='s'

				horizontal+=1
				listoflist.append(copy.deepcopy(current))
				# listoflist.append(current[:])
				curr+=1


for i in range(0,curr):
	for j in range(0,9):
		for k in range(0,9):
			print(listoflist[i][j][k], end = " ")
		print()
	print()	
# print(listoflist)



