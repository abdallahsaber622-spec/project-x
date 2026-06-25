#التحدث معه في البدايه 
print("Hello, World!")
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
age = input(" ammmm How old are you? ")
if int(age) >= 10:
    #السؤال الاول
    print(f"You are {age} years old your year is so good.")
    print ('okay i give you some question' \
    ' What is the capital of France?')
    if input() == 'Paris' or 'paris':
        print('Correct!')
        x=input('okay i can give you 1 more question? ')
        if x == 'yes' or x == 'Yes':
            #السؤال الثاني
            print("okay what is the best country from visetours in africa ")
            if input() == 'egypt' or  'Egypt':    
                print ('Correct! you are so smart')
                input('okay i can give you 1 more question? but this is for smarters only okay it' \
                'is in math and it is hard okay? or bye? ')


                if input() == 'Okay'or'okay':
                    # السؤال الثالث للاذكياء فقط
                    print('okay what is answer of this'
                    'x=15-9*21'
                    'u=51'
                    'y=15/5*20'
                    '(y+u+x)*114-655*u'
                    'you cant solive it only with paper or calcolater')
                
                    if input() == '40587':
                        print('Correct! you are so so so so smart')
                        input("do you want play a small game?? or bye [yes play,no bye]")
                        if input()=="yes play"or "Yes play":
                            # بدايه اللعبه
                            print("welcome to game ")
                            print ("this game if you answer this last questions you is smart so " \
                            "we see it in some questions what do you want We ask about him" \
                            "[math or Ask a geographer about capital cities, or an astronomy student,"
                            " or ask them random questions.]")



                    else:
                        print('Incorrect. The answer is 40587.')                
                else:
                    print ("okay bye")
                    
                   
            else:
                print('okay bye')           
        else:
            print('okay bye')
    else:
        print('Incorrect. The capital of France is Paris.')
else:    print(f"You are {age} years old your year is so bad.")

