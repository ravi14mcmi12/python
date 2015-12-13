def check_grid(infile):
# to check 1-9 in each columns
	#cols = [[row[i] for row in infile] for i in range(0,9)]
	list(infile)
	lst = infile
	lst_col = []
	no_row = len(lst)
	no_col = len(lst[0])
	for j in range(0,no_col):
		tmp = []
		for i in range(0,no_row):
			tmp.append(lst[i][j])
		lst_col.append(tmp)
	cols = lst_col
	print(cols)
	#cols = infile
	leg = 0
	for i in range(0,9):
		for j in range(0,9):
			if cols[i].count(cols[i][j]) <=1:
				leg = leg + 0
			else:
				leg = leg + 1
#to check 1-9 in each rows
	count = 0
	row = infile
	for i in range(0,9):
		for j in range(0,9):
			if row[i].count(row[i][j]) <= 1:
				count = count + 0
			else:
				count = count + 1
# to check 1-9 in each 3*3 matrix
	'''
	angle = []
	for t in range(0,3):
		ang = infile[t]
		for u in range(0,3):
			angle.append(ang[u])
			foot = 0
			for be in range(0,9):
				if angle.count(angle[be]) <= 1:
					foot = foot + 0
				else:
					foot = foot + 1
	'''
	if(count + leg) == 0:
		print("Sudoku is Valid.")
	else:
		print("Sudoku is Invalid.")
		
######################################################
def sudoko_checker():
	try:
		file = input("Enter your File name:")
		fi = open(file, "r")
		infile = fi.read()
		grid = [list(i) for i in infile.split()]
		print(grid)
		print("The total number in this puzzle is:",len(grid))
		check_grid(grid)
	except FileNotFoundError:
		print("The inputted file doesn't exist.")
###########################################################
sudoko_checker()
