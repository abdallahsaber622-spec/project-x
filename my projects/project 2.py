#البدايه السؤال الاول
print("🎲 welcome to the number guessing game!! 🎲")
import random 
number = random.randint(1,100)
attempt=0
while True:
    guess =int(input("enter a number between 1,100 "))
    if guess > number:
        print ("your guess is so high try agian : ")
        attempt+=1
    if guess < number:
        print("your guess is so low try agian : ")
        attempt+=1
    if number == guess:
        print (f"you win the number is {number} number your attempt is {attempt}")
        break
