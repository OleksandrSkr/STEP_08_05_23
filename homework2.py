number = int(input("Enter you number : "))
degree = int(input("To what degree from 0 to 7 to raise your number ? "))
if degree >= 0 and degree <= 7 :
    print(number**degree)
else:
    print("Enter a degree value from 0 to 7")