names = []
for line in open("p022_names.txt"):
	names = line.split(',')
names = [x[1:(len(x)-1)] for x in names]

names = sorted(names)

result = 0



for i in range(0, len(names)):
	
	name_len = len(names[i])
	name_val = 0
	
	for j in range(0, name_len):
		
		if names[i][j] == 'A':
			name_val = name_val + 1
		if names[i][j] == 'B':
			name_val = name_val + 2
		if names[i][j] == 'C':
			name_val = name_val + 3
		if names[i][j] == 'D':
			name_val = name_val + 4
		if names[i][j] == 'E':
			name_val = name_val + 5
		if names[i][j] == 'F':
			name_val = name_val + 6
		if names[i][j] == 'G':
			name_val = name_val + 7
		if names[i][j] == 'H':
			name_val = name_val + 8
		if names[i][j] == 'I':
			name_val = name_val + 9
		if names[i][j] == 'J':
			name_val = name_val + 10
		if names[i][j] == 'K':
			name_val = name_val + 11
		if names[i][j] == 'L':
			name_val = name_val + 12
		if names[i][j] == 'M':
			name_val = name_val + 13
		if names[i][j] == 'N':
			name_val = name_val + 14
		if names[i][j] == 'O':
			name_val = name_val + 15
		if names[i][j] == 'P':
			name_val = name_val + 16
		if names[i][j] == 'Q':
			name_val = name_val + 17
		if names[i][j] == 'R':
			name_val = name_val + 18
		if names[i][j] == 'S':
			name_val = name_val + 19
		if names[i][j] == 'T':
			name_val = name_val + 20
		if names[i][j] == 'U':
			name_val = name_val + 21
		if names[i][j] == 'V':
			name_val = name_val + 22
		if names[i][j] == 'W':
			name_val = name_val + 23
		if names[i][j] == 'X':
			name_val = name_val + 24
		if names[i][j] == 'Y':
			name_val = name_val + 25
		if names[i][j] == 'Z':
			name_val = name_val + 26

	name_score = (i + 1) * name_val

	result = result + name_score


	print((i+1), names[i], name_val, name_score, result)