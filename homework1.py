# Function to grade homework 1
def grade(module):
	module.turtleShapes()
	module.multiplicationQuiz()
	
def get_penalties():
	return {
		'1' : (-5  , "-5: Not all shapes drawn on screen."),
		'2' : (-10 , "-10: Multiplication Quiz does not exit on blank input."),
		'3' : (-10 , "-10: Turtle does not complete."),
		'4' : (-0  , "Functions should not run until called.")
	}