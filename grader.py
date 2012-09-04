import os,sys,subprocess,imp

# Make the directory to move all graded homeworks
def make_done_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
		print("making dir!")

# Function to grade homework 1
def homework1(module):
	module.turtleShapes()
	module.multiplicationQuiz()

# Grades one file
def test_file(path, name, test_func):
	full_name = path + '/' + name
	foo = imp.load_source('homework',full_name)
	homework1(foo)
	# Look at the file to check for comments and such
	subprocess.call(['less',full_name])

# Loads all files and grades them
def load_files(path):
	p = os.getcwd() + '/' + path
	dirList = os.listdir(path)
	
	grades = {}
	
	make_done_dir(p + '/graded')
	
	for fname in dirList:
		if fname[-3:] ==  '.py':
			modName = fname[:-3]
			test_file(path,fname,homework1)
			g = input("Grade?    ")
			c = input("Comment?    ")
			grades[modName] = (g,c)
			subprocess.call(['mv',p+'/'+fname,p+'/graded'])
			cont = input("Continue?    ")
			# Even the best TAs sometimes need a break!
			if cont:
				break
	return grades

if __name__ == '__main__':
	d = input("Which directory should we read from?    ")
	grades = load_files(d)
	for k in grades:
		print('\n*********\n')
		print(k + ':    ' + grades[k][0] + '\n\n' + grades[k][1])