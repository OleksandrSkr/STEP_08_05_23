print("Enter the cost of 1 second of phone conversation for different operators, UA/second")

tariffs = {
    "KyivStar-KyivStar" : input("Enter tariff KyivStar-KyivStar : "),
    "KyivStar-Vadafon" : input("Enter tariff KyivStar-Vadafon : "),
    "KyivStar-Life" :  input("Enter tariff KyivStar-Life : "),
    "Vadafon-Vadafon" :  input("Enter tariff Vadafon-Vadafon : "),
    "Vadafon-KyivStar" :  input("Enter tariff Vadafon-KyivStar : "),
    "Vadafon-Life" :  input("Enter tariff Vadafon-Life : "),
    "Life-Life" :  input("Enter tariff Life-Life : "),
    "Life-KyivStar" :  input("Enter tariff Life-KyivStar : "),
    "Life-Vadafon" :  input("Enter tariff Life-Vadafon : "),
}
print("Select the operator from which you will call and the operator to whom you will call")

call_operator = input("""
    1) KyivStar-KyivStar
    2) KyivStar-Vadafon
    3) KyivStar-Life
    4) Vadafon-Vadafon
    5) Vadafon-KyivStar 
    6) Vadafon-Life
    7) Life-Life
    8) Life-KyivStar
    9) Life-Vadafon
""")
call_time = input("Enter the time of the phone call second : " )

if call_operator == "1":
    cost = int(call_time) * float(tariffs["KyivStar-KyivStar"])
    print("The cost of a telephone conversation is UA : ", + cost)
elif call_operator == "2":
    cost = int(call_time) * float(tariffs["KyivStar-Vadafon"])
    print("the cost of a telephone conversation is UA : ", + cost)
elif call_operator == "3":
    cost = int(call_time) * float(tariffs["KyivStar-Life"])
    print("the cost of a telephone conversation is UA : ", + cost)
elif call_operator == "4":
    cost = int(call_time) * float(tariffs["Vadafon-Vadafon"])
    print("the cost of a telephone conversation is UA : ", + cost)
elif call_operator == "5":
    cost = int(call_time) * float(tariffs["Vadafon-KyivStar"])
    print("the cost of a telephone conversation is UA : ", + cost)
elif call_operator == "6":
    cost = int(call_time) * float(tariffs["Vadafon-Life"])
    print("the cost of a telephone conversation is UA : ", + cost)
elif call_operator == "7":
    cost = int(call_time) * float(tariffs["Life-Life"])
    print("the cost of a telephone conversation is UA : ", + cost)
elif call_operator == "8":
    cost = int(call_time) * float(tariffs["Life-KyivStar"])
    print("the cost of a telephone conversation is UA : ", + cost)
elif call_operator == "9":
    cost = int(call_time) * float(tariffs["Life-Vadafon"])
    print("the cost of a telephone conversation is UA : ", + cost)
else:
    print("You have not selected the correct operators, try again")
