import imp
import subprocess
import datetime

argList = [
    [ [ None, None, None], 15 ],
    [ [ 'TeamA', None, None ], 5 ],
    [ [ 'TeamB', None, None ], 10 ],
    [ [ None, 2000, 2005 ], 15 ],
    [ [ None, 2000, None ], 15 ],
    [ [ None, None, 2005 ], 15 ],
    [ [ None, None, 2003 ], 7 ],
    [ [ None, 2001, 2003 ], 6 ],
    [ [ None, 2003, None ], 12 ],
    [ [ 'TeamA', 2003, None ], 4 ],
    [ [ 'TeamB', 2003, None ], 8 ],
    [ [ 'TeamB', 2000, 2005 ], 10 ]
]

def call_func(function,args):
    if args[0] and args[1] and args[2]:
        return function(team=args[0],startyear=args[1],endyear=args[2])
    
    if args[0] and args[1]:
        return function(team=args[0],startyear=args[1])
    if args[0] and args[2]:
        return function(team=args[0],endyear=args[2])
    if args[1] and args[2]:
        return function(startyear=args[1],endyear=args[2])
    
    if args[0]:
        return function(team=args[0])
    if args[1]:
        return function(startyear=args[1])
    if args[2]:
        return function(endyear=args[2])
    
    return function()

# Function to grade homework 1
def grade(module,file_name):

    date = datetime.date.today() - datetime.timedelta(days=365*32)
    try:
        player = module.BasketballPlayer('id0','joe','blow',1999,2005,date)
    except Exception as e:
        print(e)
        try:
            player = module.BasketBallPlayer('id0','joe','blow',1999,2005,date)
        except Exception as e2:
            print(e2)
            print("ERROR making player")
    try:
        player.addseason("TeamA",2000,1)
        player.addseason("TeamB",2001,2)
        player.addseason("TeamA",2003,4)
        player.addseason("TeamB",2004,8)
    except Exception as e:
        print(e)
        print("ERROR adding seasons")

        

    try:
        p = module.BasketballPlayer.findplayer('id0')#ABRAMJO01')
        if not p:
            raise Exception()
    except Exception as e:
        p = None
        print(e)
        print("ERROR finding player")
    try:
        print(p.playerid)
        print(p.birthdate)
        print(p.retirementage)
    except:
        print('ERROR getting attributes')
    print('')

    for arg in argList:
        print(arg)
        try:
            c = call_func(p.gamesplayed,arg[0])
            print(c)
            if c == arg[1]:
                print('PASS')
            else:
                print('FAIL')
        except Exception as e:
            print("ERROR Getting Data")
            print(e)

        input()
    input()
    
def get_penalties():
	return {
		1  : (-5  , "Insufficient Comments."),
		2  : (-20 , "Code has syntax errors, fix for partial credit"),
        3  : (-40 , "Error making player (No further functionality could be tested, fix for partial credit)"),
        4  : (-20 , "Error adding seasons (No further functionality could be tested, fix for partial credit)"),
        5  : (-20 , "Error getting by ID"),
        6  : (-10 , "Error getting attributes"),
        7  : (-10 , "Error calling  gamesplayed, fix for partial credit"),
        8  : (-10 , "Incorrect results for gamesplayed")
	}
