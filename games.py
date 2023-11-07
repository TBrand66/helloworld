#  Guessing game


secret_number = 9
count = 0
guess_limit = 3

while count < guess_limit:
   guess = int(input('Guess: '))
   count += 1
   if guess == secret_number:
        print('You won!')
        break
else:
    print('Better luck next time')


## build a simple commands for a car

command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started..")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("car already stopped..")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry, i dont understand you")
