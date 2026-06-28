#والله يا اخي عملتهه بس هضيف عليا شويه حجات
# دي تفهه خالص

print("___Age in days cacolator___")
year= int (input("enter your age in years please: "))
print(f"your age with days is { year*365 }")
# الاضافات
monthes =str(input ("do you want to now your age by monthes??? : [yes,no] "))

if monthes== "yes" :
    years = int( input("okay print your age with years please: "))
    print(f"your age with monthes  is : {years*12}") 
    #بالساعات
    hours=int(input (" hmmmm i know you want to know your age with ahoursokay pls print your age " \
    "okay pls print your age "))
    print (f"your age with hours is {hours*8760} you have many good hours in your life pro"\
        f" you you have {hours * 8760} hours aomy gad ")
else:
    print( "okay bye")



