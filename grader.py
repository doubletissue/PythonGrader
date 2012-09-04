import os,sys,subprocess,imp
import pyperclip

def assign_grade(penalties):
	score = 100
	comment = ''
	added = set()
	while True:
		print('current score: ' + str(score))
		print('current comment: ' + comment)
		for k in sorted(penalties.keys()):
			print(k + ':   ' + str(penalties[k][0]) + ' , ' + penalties[k][1])
		print('new')
		p = input("which penalty?    ")
		if not p:
			return (score,comment,penalties)
		if p == 'new':
			s = input('points?    ')
			c = input('comment?    ')
			k = input('key?    ')
			score += int(s)
			comment += c + '\n'
			penalties[k] = (int(s),c)
			added.add(k)
		if p in penalties and p not in added:
			added.add(p)
			score += penalties[p][0]
			comment += penalties[p][1] + '\n'

# Make the directory to move all graded homeworks
def make_done_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
		print("making dir!")

# Grades one file
def test_file(path, name, test_func):
	full_name = path + '/' + name
	foo = imp.load_source('homework',full_name)
	test_func(foo)
	# Look at the file to check for comments and such
	subprocess.call(['less',full_name])

# Loads all files and grades them
def load_files(path):
	p = os.getcwd() + '/' + path
	dirList = os.listdir(path)
	
	grades = {}
	
	make_done_dir(p + '/graded')
	
	homework = __import__('homework' + path)
	
	penalties = homework.get_penalties()
	
	for fname in dirList:
		if fname[-3:] ==  '.py':
			print("**********\n" + fname + "\n*********")
			modName = fname[:-3]
			test_file(path,fname,homework.grade)
			#g = input("Grade?    ")
			#c = input("Comment?    ")
			g,c,n = assign_grade(penalties)
			penalties = n
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
	for k in sorted(grades.keys()):
		print('\n*********\n')
		print(k + ':    ' + str(grades[k][0]) + '\n\n' + grades[k][1])
		pyperclip.copy(grades[k][1])
		input('')