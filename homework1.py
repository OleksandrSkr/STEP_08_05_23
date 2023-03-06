i = int(input("Enter a number from 1 to 100 : "))
if i < 1 or i > 100 :
    print("You entered an incorrect number, try again ")
elif (i%3 ==0) and (i%5 ==0):
    print("Fizz Buzz")
elif (i%3 == 0):
    print("Fizz")
elif (i%5 == 0):
    print("Buzz")
else:
    print(i)