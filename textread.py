state = open("status.txt", "r")
parse = state.read()
if (parse) == 'TEXT':
    print('TRUE')
else:
    print ('FALSE')
    
state.close()
