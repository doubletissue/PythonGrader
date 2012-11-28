import imp
import subprocess

args = [ ['--help'],
         ['-h'],
         [],
         ['-m'],
         ['--modified'],
         ['-o','name'],
         ['-o','n'],
         ['-o','modified'],
         ['-o','m'],
         ['-o','size'],
         ['-o','s'],
         ['--order=s'],
         ['-r'],
         ['--recursive'],
         ['-s'],
         ['--sizes'],
         ['-m','-o','m'],
         ['-o','s','-s'],
         ['-m','-r','-s'],
         ['-m','-s','-r'],
         ['-m','-s','-r','-o','s'],
         ['homework5'],
         ['homework5','homework4'],
         ['-s','homework5'],
    ]

# Function to grade homework 1
def grade(module,file_name):
    print(subprocess.check_output(['clear','&&','clear']).decode('utf-8'))
    for add_args in args:
        sys_args = ['python',file_name]
        sys_args.extend(add_args)
        print(sys_args)
        try:
            print(subprocess.check_output(sys_args).decode('utf-8'))
        except:
            print("ERROR!")
        print('\n\n\n')
        c = input()
    
def get_penalties():
	return {
		1  : (-5  , "Insufficient Comments."),
		2  : (-20 , "Code has syntax errors."),
        3  : (-10 , "Error with ordering"),
        4  : (-10 , "Error with listing size"),
        5  : (-10 , "Error with recursion"),
        6  : (-10 , "Error with modification date"),
        7  : (-5  , "Error with taking both long and short arguments"),
        8  : (-10 , "Error using one alternate directory"),
        9  : (-5 , "Error using two alternate directories"),
	}
