command = ""
isCarStarted = False
isCarStopped = True

while command.lower() != 'exit':
    command = input("Enter command: ")
    if command.lower() == 'help':
        print('''Available commands:
              - start : To start the car
              - stop: To stop the car
              - exit : To exit the game..''')
    elif command.lower() == 'start':
        if isCarStarted:
            print("Car is already started!")
        else:
            isCarStarted = True
            isCarStopped = False
            print("The Car has now been Started!")
    elif command.lower() == 'stop':
        if isCarStopped:
            print("Car is already stopped!")
        else:
            isCarStopped = True
            isCarStarted = False
            print("The car has now been Stopped!")
    else:
        print("I don't understand that command.")