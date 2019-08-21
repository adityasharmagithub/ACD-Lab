#develop a DFA for T = a,b accepting strings with 'abba' as a substring

state =  0
string = input("Enter a string :")

print("State Traversing Sequence: ")
print("q 0")

if string != '':
	for i in string:
		if state == 0 and i == 'a':
			state = 1
			print("q 1")
		elif state == 0 and i == 'b':
			state = 0
			print("q 0")
		elif state == 1 and i == 'a':
			state = 1
			print("q 1")
		elif state == 1 and i == 'b':
			state = 2
			print("q 2")
		elif state == 2 and i == 'a':
			state = 1
			print("q 1")
		elif state == 2 and i == 'b':
			state = 3
			print("q 3")
		elif state == 3 and i == 'a':
			state = 4
			print("q 4")
		elif state == 3 and i == 'b':
			state = 0
			print("q 0")
		elif state == 4:
			state = 4
			print("q 3")

if state == 4:
	print("String is valid and accepted!")
else:
	print("Can't accept the string!")
