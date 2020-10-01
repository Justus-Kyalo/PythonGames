#color=input("enter a color:")
#plural_noun= input("enter a plural noun:")
#celebrity= input("enter a plural noun:")
#print("roses are " + color)
#print(plural_noun + " are blue")
#print("i love " + celebrity)
#friends=["kevin","karen","jim","toby","oscar"]
#lucky_numbers=[0,1,3,4,5,7,10]
#friends[0]="mike"
#friends.append("kim")
#friends.insert(1,"kelly")
#friends.remove("jim")
#friends.pop()
#friends.clear()
#print(friends.count("jim"))
#print(friends.index("kevin"))
#friends.sort()
#friends2=friends.copy()
#lucky_numbers.reverse()

#friends.extend(lucky_numbers)
#print(friends)


#coordinates=[(2,5),(3,2),(1,9)]
#print(coordinates[0])

#def sayhi():
    #print("top")

   # print("hello user")
#sayhi ()
#print("bottom")
#def say_hi(name,age):
 #   print("hello  "+ name +" you are "+ age)
#say_hi( "mike" ,"70")

#or
   #  print("hello " + name +" you are " +str( age))
#say_hi("mike", 70)

#def cube(num):
 #   return num*num* num
#print(cube(4))
#or
#result=cube(4)
#print(result)

#if statements
#is_tall=True
#is_male=True
#if is_male and is_tall:
#    print("male and tall")
#elif not is_male and is_tall:
#    print("not male but tall")
#elif is_male and not is_tall:
#    print("is male but not tall")
#elif is_male or is_tall:
#    print("either male or tall or both")
#else:
#    print("neither a male nor tall")


#if statements and comparisons
#def max_num(num1,num2,num3):
 #   if num1>=num2 and num1>=num3:
  #      return num1
   # elif num2>=num1 and num2>=num3:
    #    return num2
    #else:
     #   return num3
#print(max_num(30,20,40))

#BUILDING A BETTER CALCULATOR
#num1=float(input("enter a number:"))
#op=input("enter operator:")
#num2=float(input("enter   a number:"))
#if op=="+":
#    print(num1+num2)
#elif op=="-":
#    print(num1-num2)
#elif op=="/":
#    print(num1/num2)
#elif op=="*":
#    print(num1*num2)
#else:
#    print("invalid operator")


#DICTIONARIES
#monthConversions={
#"jan":"january",
#"feb":"february",
#"mar":"march",
#"apr":"april",
#}
#print(monthConversions["mar"])


#WHILE LOOP
#i=0
#while i<=10:
 #   print(i)
 #   i+=1
# BUILDING A GUESSING GAME
#secret_word="giraffe"
#guess=""
#while guess!=secret_word:
#    guess=input("enter a guess:")
#print("you win!!")
#SETTING A FIXED NUMBER OF GUESSES
#secret_word="giraffe"
#guess=""
#guess_count=0
#guess_limit=3
#out_of_guess=False
#while guess!=secret_word and not (out_of_guess):
#    if guess_count<guess_limit:
#        guess=input("enter a guess")
#        guess_count+=1
#    else:
#        out_of_guess=True
#if out_of_guess:
#    print("out of guess,YOU LOSE!!")
#else:
#    print("YOU WIN!!")


#FOR LOOP
#for letter in "giraffe academy" :
 #   print(letter)
friends=["jim","karen","kevin"]
#for name in friends:
#     print(name)

#for index in range(10):
 #   print(index)

#for index in range (2,10):
     #print(index)

#len(friends)
#or
#for index in range(len(friends)):
#         print(friends[index])

#for index in range (5):
    #if index==0:
    #    print("first iteration")
    #else:
        #print("not first iteration")

#EXPONETIAL FUNCTIONS
#print(2**3)
#
#def raise_to_power(base_num,power_num):
#    result=1
#    for index in range(power_num):
#        result=result*base_num
#    return result
#print(raise_to_power(3,4))

#2D LISTS AND NESTED LOOPS
#number_grid=[ (0,1,2),(3,6,5),(4,5,1)]
#print(number_grid[0][0])

#for row in number_grid:
#    for col in row:
#        print(col)

#BUILD A TRANSLATOR
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"g"
        else:
            translation=translation+letter
    return translation
print(input("enter phrase:"))