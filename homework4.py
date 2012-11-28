import imp

def grade(module,file_name):
    print('*********\nFILE\n*********')
    try:
        print(module.get_dictionary('test.txt',type_ = 'file'))
        print('')
        print(module.get_dictionary('test.txt',type_ = 'file', single_word = True))
        print('')
        print(module.get_dictionary('test.txt',type_ = 'file', single_word = False))
        print('')
    except Exception as e:
        print(e)
        print("Error getting File")

    print('*********\nTEXT\n*********')
    try:
        print(module.get_dictionary('hello this is\na test',type_ = 'text'))
        print('')
        print(module.get_dictionary('hello this is\na test',type_ = 'text', single_word = True))
        print('')
        print(module.get_dictionary('hello this is\na test',type_ = 'text', single_word = False))  
        print('')
    except Exception as e:
        print(e)
        print("Error getting Text")
    
    print('*********\nURL\n*********')
    try:
        print(module.get_dictionary('http://loripsum.net/api/plaintext',type_ = 'url'))
        print('')
        print(module.get_dictionary('http://loripsum.net/api/plaintext',type_ = 'url', single_word = True))
        print('')
        print(module.get_dictionary('http://loripsum.net/api/plaintext',type_ = 'url', single_word = False))
        print('')
    except Exception as e:
        print(e)
        print("Error getting URL")

    
    print('*********\nCOMPUTER PLAYER\n*********')
    try:
        d = module.get_dictionary('this is a test',type_='text')
        module.play_against_computer_guesser(solution='test', dictionary=d)
        module.play_against_computer_guesser(solution='test', dictionary=d, guesses=['t','a','b','s','e','t'])
    except Exception as e:
        print(e)
        print("Error playing computer")

    print('*********\nHUMAN PLAYER\n*********')
    try:
        d = module.get_dictionary('ahoy matey',type_='text')
        module.play_against_human_guesser(solution='test')
        module.play_against_human_guesser(solution='test')
        module.play_against_human_guesser(solution='a test')
        module.play_against_human_guesser(dictionary=d)
    except Exception as e:
        print(e)
        print("Error playing human")
    
    
def get_penalties():
	return {
		1  : (-5  , "Insufficient Comments."),
		2  : (-20  , "Code has syntax errors."),
		3  : (-10  , "Error using test source."),
		4  : (-10  , "Error using file source."),
		5  : (-10  , "Error using url source."),
		6  : (-10  , "Error with computer player."),
		7  : (-10  , "Error with human player.")
	}
