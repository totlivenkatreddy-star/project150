users  = ["venkat","reddy ", "totli", 2, 3,4,5,6]
#append method in list
users.append("tvr")

print(users)
for i in users:
    print(i)
#insert method in list
users.insert(2,"babu") 
print(users)   

#remove method in list

users.remove("babu")
print(users)

#remove by index
users.pop(3)
print(users)

#length method in list
print(len(users))