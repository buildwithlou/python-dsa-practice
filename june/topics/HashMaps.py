#Hashmaps are collections of key-value pairs using dictionaries
person = {
    "name": "Carlos",
    "age": 25,
    "city": "Miami"
}

# print(person["name"])   # Carlos — crystal clear what this is
# print(person["age"])    # 25

for key,value in person.items(): #items gives us key and value pairs (same time)
    print(key, ":", value)

print(person.get("phone", "Not found")) # GET method allows us to provide a default value if the key is not found

##Real life Example
fruits = ["apple", "banana", "orange", "apple", "banana", "apple"] #this is a list of fruits with duplicates

count = {} #empty dictionary to store the count of each fruit

for fruit in fruits: #we go through each fruit in the list
    if fruit in count: #if we have already seen this fruit, we increment the count
        count[fruit] = count[fruit] + 1
    else:
        count[fruit] = 1 #if we haven't seen this fruit before, we add it to the dictionary with a count of 1
    
print(count) #this will print the count of each fruit in the list