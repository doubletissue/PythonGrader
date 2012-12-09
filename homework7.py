import subprocess

# Function to grade homework 1
def grade(module,file_name):
    try:
        s = subprocess.check_output(['python',file_name]).decode('utf-8')
        print(s)
    except Exception as e:
        print("ERROR!")
        print(e)
				
	
def get_penalties():
	return {
		1  : (-70  , "No shapes appear."),
		2  : (-60  , "Shapes do not fall."),
		3  : (-15  , "Shapes do not move sideways."),
		4  : (-15  , "Shapes do not rotate."),
		5  : (-20  , "Shapes can leave the baord."),
		6  : (-30  , "New shapes not added."),
		7  : (-20  , "Rows are not removed."),
		8  : (-20  , "Loser not detected."),
        9  : (-10  , "Not enough comments")
	}
