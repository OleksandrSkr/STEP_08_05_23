#manager_John = input("Enter the sales manager John level $ : ")
#print("Sales manager John level = " + manager_John)
#manager_Bob = input("Enter the sales manager Bob level $ : ")
#manager_Mike = input("Enter the sales manager Mike level $ : ")

#managers = max(int(manager_John), int(manager_Bob) , int(manager_Mike))
#best_manager = max(manager_John, manager_Bob , manager_Mike)
#print(managers)

managers = []

manager_1 = {
    "name" : input("Enter name first manager : "),
    "sales" : input("Enter sales first manager : ")
}
managers.append(manager_1)
manager_2 = {
    "name" : input("Enter name second manager : "),
    "sales" : input("Enter sales second manager : ")
}
managers.append(manager_2)
manager_3 = {
    "name" : input("Enter name third manager : "),
    "sales" : input("Enter sales third manager : ")
}
managers.append(manager_3)
print(managers)
i = 0

while i < len(managers):
    manager = managers[i] 
    print(manager["name"])
    i += 1