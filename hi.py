print("Hello, World!")
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
age = input(" ammmm How old are you? ")
if int(age) >= 10:
    print(f"You are {age} years old your year is so good.")
    print ('okay i give you some question' \
    ' What is the capital of France?')
    if input() == 'Paris' or 'paris':
        print('Correct!')
        x=input('okay i can give you 1 more question? ')
        if x == 'yes' or x == 'Yes':
            print("okay what is the best country from visetours in africa ")
            if input() == 'egypt' or input() == 'Egypt':    
                print ('Correct! you are so smart')
        else:
            print('okay bye')

    else:
        print('Incorrect. The capital of France is Paris.')



else:    print(f"You are {age} years old your year is so bad.")

