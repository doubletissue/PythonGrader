# Function to grade homework 1
def grade(module,file_name):
	try:
		module.turtleShapes()
	except:
		print("Unable to test the turtle!")
	try:
		module.multiplicationQuiz()
	except:
		print("Unable to test the quiz!")
	
def get_penalties():
	return {
		1  : (-0  , "Not all shapes drawn on screen."),
		2  : (-10 , "Multiplication Quiz does not exit on blank input."),
		3  : (-10 , "Turtle does not complete."),
		4  : (0   , "Functions should not run until called."),
		5  : (0   , "Comment containing name missing from beginning of code."),
		6  : (0   , "Insufficient comments for Turtle code."),
		7  : (0   , "Insufficient comments for Multiplication Quiz code."),
		8  : (0   , "Incorrectly named file."),
		9  : (0   , "Late submission."),
		10 : (-30 , "Code has syntax errors.")
	}
