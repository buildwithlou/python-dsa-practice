import math
print(math.sqrt(16))
print(math.pi)

import random
print(random.randint(1,10))



import datetime
print(datetime.date.today())



# import os ##Talk to your operating system
# print(os.getcwd()) #current directory
# print(os.listdir(".")) #list of files in current directory
# print(os.mkdir("new_folder")) #create a new folder called "new_folder"
# print(os.path.exists("file.txt"))  #check if a file called "file.txt" exists in the current directory
# print(os.path.join("folder", "file.txt"))   #join two paths together, in this case it will return "folder/file.txt"
# print(os.getenv("HOME")) #get the value of the environment variable "HOME"

# import sys ##Talk to Python itself
# sys.version #get the version of Python you are using
# sys.argv #get the list of command line arguments passed to the script
# sys.exit() #exit the program
# sys.path #get the list of directories Python searches for modules

# import json ##Work with JSON data
# data = {"name": "Lourdes", "age": 25}
# json_string = json.dumps(data) #convert a Python object to a JSON string
# print(json_string)

# parsed = json.loads(json_string) #convert a JSON string back to a Python object
# print(parsed["name"]) #access the "name" value from the parsed JSON data

# with open("data.json", "w") as f: #write JSON data to a file
#     json.dump(data, f)

# with open("data.json", "r") as f: #read JSON data from a file
#     data_from_file = json.load(f)

from collections import Counter, defaultdict, deque

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words) #count the frequency of each word in the list
print(count)
print(count.most_common(2)) #get the two most common words

scores = defaultdict(int) #create a defaultdict with int as the default factory
scores["Lourdes"] += 10 #increment the score for "Lourdes" by 10
print(scores["Lourdes"]) #print the score for "Lourdes"

queue = deque([1,2,3]) #create a deque (double-ended queue)
queue.appendleft(0) #add an element to the left end of the deque
queue.pop() #remove and return an element from the right end of the deque
print(queue) #print the current state of the deque