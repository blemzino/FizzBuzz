msg = print("FizzBuzz program I made, please enter what number you would like it to count up to.\n")
userinput = int(input("Enter number:\n"))

for i in range(userinput): 
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz!") 
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)
    
# Program loops through the number given by the user from var userinput
# "if i % 3 == 0 and i % 5 == 0" was put first due to the fact that if it was put after the other two "if" statements and next in loop was a number divisible by both 3 and 5, the program would not check because the condition was already met, because the number was divisible by either 3 or 5.  
