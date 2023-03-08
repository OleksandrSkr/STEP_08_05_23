manager_1 = {
    "name" : input("Enter name first manager : "),
    "sales" : input("Enter sales first manager : ")
}

manager_2 = {
    "name" : input("Enter name second manager : "),
    "sales" : input("Enter sales second manager : ")
}

manager_3 = {
    "name" : input("Enter name third manager : "),
    "sales" : input("Enter sales third manager : ")
}

print(manager_1)
print(manager_2)
print(manager_3)
#print(managers["sales"])

if int(manager_1["sales"]) > int(manager_2["sales"]):
    if int(manager_1["sales"]) > int(manager_3["sales"]):
        best_manager = manager_1["name"]
        best_sales = manager_1["sales"]
        print("best manager : "   + best_manager)
    else:
        best_manager = manager_3["name"]
        best_sales = manager_3["sales"]
        print("best manager : "  + best_manager)
else:
    if int(manager_2["sales"]) > int(manager_3["sales"]):
        best_manager = manager_2["name"]
        best_sales = manager_2["sales"]
        print("best manager : " +  best_manager)
    else:
        best_manager = manager_3["name"]
        best_sales = manager_3["sales"]
        print("best manager : " + best_manager)