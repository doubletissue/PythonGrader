import subprocess

# Function to grade homework 1
def grade(module,file_name):
	try:
		while True:
			print(dir(module))
			func = input("Which function to run? EXEC to run file    ")
			if func == 'EXEC':
				s = subprocess.check_output(['python',file_name]).decode('utf-8')
				print(s)
			elif func == 'EXEC2':
				s = subprocess.check_output(['python',file_name,'player_career.csv']).decode('utf-8')
				print(s)
			elif func == '':
				break
			else:
				try:
					getattr(module,func)()
				except Exception as e:
					print("Function did not work")
					print(e)
	except Exception as e:
		print("error loading module")
		print(e)
				
	
def get_penalties():
	return {
		1  : (-20  , "Incorrect Statistics."),
		2  : (-10 , "Table improperly formatted."),
		3  : (-5   , "Comment containing name missing from beginning of code."),
		4  : (-10   , "Insufficient comments for code."),
		5  : (-5   , "Incorrectly named file."),
		6  : (-20   , "Late submission."),
		7  : (-30 , "Code has syntax errors."),
		8  : (-20 , "Late, will not be graded from Assignment 3 forward.")
	}