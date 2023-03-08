manager_f = {
    "manager" : input("Enter name first manager : "),
    "sales" : input("Enter sales first manager : "),
    "money" : 0 ,
    "reword" : 0
}
sales_f = int(manager_f["sales"])
if sales_f <= 500:
    money_f = 200 + 0.03*sales_f
elif sales_f > 500 and sales_f <= 1000:
    money_f = 200 + 0.05*sales_f
else:
    money_f = 200 + 0.08*sales_f
manager_f["money"] = money_f

manager_s = {
    "manager" : input("Enter name second manager : "),
    "sales" : input("Enter sales second manager : "),
    "money" : 0 ,
    "reword" : 0
}
sales_s = int(manager_s["sales"])
if sales_s <= 500:
    money_s = 200 + 0.03*sales_s
elif sales_s > 500 and sales_s <= 1000:
    money_s = 200 + 0.05*sales_s
else:
    money_s = 200 + 0.08*sales_s
manager_s["money"] = money_s

manager_t = {
    "manager" : input("Enter name third manager : "),
    "sales" : input("Enter sales third manager : "),
    "money" : 0 ,
    "reword" : 0
}
sales_t = int(manager_t["sales"])
if sales_t <= 500:
    money_t = 200 + 0.03*sales_t
elif sales_t > 500 and sales_t <= 1000:
    money_t = 200 + 0.05*sales_t
else:
    money_t = 200 + 0.08*sales_t
manager_t["money"] = money_t


if int(manager_f["sales"]) > int(manager_s["sales"]):
    if int(manager_f["sales"]) > int(manager_t["sales"]):
        best_manager = manager_f["manager"]
        print("best manager : "   + best_manager)
        manager_f["reword"] = 200
    else:
        best_manager = manager_t["manager"]
        print("best manager : "  + best_manager)
        manager_t["reword"] = 200
else:
    if int(manager_s["sales"]) > int(manager_t["sales"]):
        best_manager = manager_s["manager"]
        print("best manager : " +  best_manager)
        manager_s["reword"] = 200
    else:
        best_manager = manager_t["manager"]
        print("best manager : " + best_manager)
        manager_t["reword"] = 200

print(manager_f)
print(manager_s)
print(manager_t)
        

