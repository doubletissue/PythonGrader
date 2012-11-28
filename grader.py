import os,sys,subprocess,imp
import pyperclip
import pep8
import sys

def assign_grade(path,penalties):
	score = 100
	comment = ''
	added = set()
	while True:
		print('current score: ' + str(score))
		print('current comment:\n' + comment)
		for k in sorted(list(set(penalties.keys()).difference(added))):
			print(str(k) + ':   ' + str(penalties[k][0]) + ' , ' + penalties[k][1])
		print('new')
		p = input("which penalty?    ")
		if not p:
			s = subprocess.check_output(['python','pep8.py',path]).decode('utf-8')
			count = s.count('\n')
			p = -(count//10)
			if p < -5:
				p = -5
			
			comment += str( p ) + ': ' + str(count) + ' PEP8 Violations\n'
			
			
			c = input('Additional Comment?    ')
			if c:
				comment += "\n\n" + str(c)
				
			comment += '\n\n---------\n\n'
			comment += "PEP8 style violations, " + str(count) + " Violations:\n\n" + s
			score += p
			if len(comment) > 2000:
				comment = comment[:2000]
				comment = comment[:comment.rfind('\n')]
				comment += "\n\nCut off due to LMS length restrictions"
			return (score,comment,penalties)
		if p == 'new':
			s = input('points?    ')
			c = input('comment?    ')
			k = int(input('key?    '))
			score += int(s)
			comment += str(s) + ': ' + str(c) + '\n'
			penalties[k] = (int(s),c)
			added.add(k)
		try:
			p = int(p)
		except:
			pass
		if p in penalties and p not in added:
			added.add(p)
			score += penalties[p][0]
			comment += str(penalties[p][0]) + ': ' + penalties[p][1] + '\n'

# Make the directory to move all graded homeworks
def make_done_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
		print("making dir!")

# Grades one file
def test_file(path, name, test_func):
	full_name = path + '/' + name
	subprocess.call(['less',full_name])
	#try:
	foo = imp.load_source('homework',full_name)
	test_func(foo,full_name)
    #except Exception as e:
	#print(e)
	# Look at the file to check for comments and such
	subprocess.call(['less',full_name])

# Loads all files and grades them
def load_files(path):
	p = os.getcwd() + '/' + path
	dirList = os.listdir(path)
	
	grades = {}
	
	make_done_dir(p + '/graded')
	
	try:
		del homework
	except:
		print("Couldn't del homework")
	
	homework = __import__(path)
	
	penalties = homework.get_penalties()
	
	for fname in dirList:
		if fname[-3:] ==  '.py':
			print("**********\n" + fname + "\n*********")
			modName = fname[:-3]
			test_file(path,fname,homework.grade)
			g,c,n = assign_grade(path+'/'+fname,penalties)
			penalties = n
			grades[modName] = (g,c)
			print('\n\n\n')
			print(modName + ':    ' + str(g) + '\n\n' + str(c))
			pyperclip.copy(str(c))
			input('')
			subprocess.call(['mv',p+'/'+fname,p+'/graded'])
			cont = input("Continue?    ")
			# Even the best TAs sometimes need a break!
			if cont:
				break
	return grades

if __name__ == '__main__':
	#d = input("What are we grading?    ")
	grades = load_files(sys.argv[1])
	'''for k in sorted(grades.keys()):
		print('\n*********\n')
		print(k + ':    ' + str(grades[k][0]) + '\n\n' + grades[k][1])
		pyperclip.copy(grades[k][1])
		input('')
	'''
