import imp

def grade(module,file_name):
    for i in range(5):
        q = input()
        print(q)
        del module
        module = imp.load_source('homework',file_name)
        module.play(module.getusermove,module.getusermove)
        #module.printboard(b)
    del module
    module = imp.load_source('homework',file_name)
    #module.play(module.getcomputermove,module.getcomputermove)
    #module.printboard(b)
    
    
def get_penalties():
	return {
		1  : (-10  , "Insufficient Comments."),
		2  : (-5   , "No Comment with name at top of file."),
		3  : (-5   , "Board should be cleared upon starting a new game."),
		4  : (-5   , "Quit should not exit program."),
		5  : (-10  , "Error detecting winner."),
		6  : (-10  , "Error making valid move."),
		7  : (-5   , "Error undoing move."),
		8  : (-5   , "Error quitting."),
		9  : (-5   , "Error resetting board."),
		10 : (-10  , "Error getting computer move."),
		11 : (-30  , "Code has syntax errors."),
		12 : (-20  , "Late."),
		13 : (-10  , "Error printing board.")
	}
