
started = False

while True:
    command = input('> ').lower()
    if command == 'start':
        if started == True:
            print('Car is already started')
        else:
            started = True
            print('Car started')
    elif command == 'stop':
        if not started:
            print('Already stopped')
        else:
            started = False
            print('Car stopped')
    elif command == 'help':
        print("""
start - to start 
stop - to stops
quit - quit program
        """)
    elif command == 'quit':
        break
    else:
        print('Sorry I dont understand')
