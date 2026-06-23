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
            if input() == 'egypt' or  'Egypt':    
                print ('Correct! you are so smart')
                input('okay i can give you 1 more question? but this is for smarters only okay it' \
                'is in math and it is hard okay? or bye? ')
                if input() == 'Okay' or 'okay':
                    print('okay what is answer of this'
                    'x=15-9*21'
                    'u=51'
                    'y=15/5*20'
                    '(y+u+x)*114-655*u'
                    'you cant solive it only with paper or calcolater')
                
                    if input() == '40587':
                        print('Correct! you are so so so so smart')
                        input("do you want alse come at 12:00pm to see more")
                    else:
                        print('Incorrect. The answer is 40587.')                
                else:
                    print ("")
                    
                   
            else:
                    print('okay bye')            




        else:
            print('okay bye')

    else:
        print('Incorrect. The capital of France is Paris.')



else:    print(f"You are {age} years old your year is so bad.")

