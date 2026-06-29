import time
#الجزء الخاص بالسؤال
print("Welcome to alarm clock")

minutes = int(input("Please enter time with minutes: "))
mode = input("Play or Learn: ").lower()
#جزء لو هيلعب 
if mode == "play":
    seconds = minutes * 60

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60

        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("Play time is over")

else:
    print("Invalid choice run again and print time")
#جزء لو هيزاكر
if mode == "learn":
    seconds = minutes * 60

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60

        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("learn time is over")
    x= input ("ohhh you need to get some time for playing okay ")
    if x =="okay":
        l= input("enter rest time ")

        seconds = minutes * 60

        while seconds > 0:
            mins = seconds // 60
            secs = seconds % 60

            print(f"{mins:02}:{secs:02}", end="\r")
            time.sleep(1)
            seconds -= 1
        print ("rest time over go and run agian to get learn time")
    else:
        print("okay bye see you soon ")
else:
    print("Invalid choice run again and print time")


