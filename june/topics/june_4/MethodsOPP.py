###__repr__ tehcnical for developers. shows how to recreate the object
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"{self.name} (grade: {self.grade})"
    def __repr__(self):
        return f"Student('{self.name}', {self.grade})"
    
s = Student("Carlos", 95)
print(s)
print(repr(s))

###__len__ makes your object work with len() (length)
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def __len__(self):
        return len(self.songs)
    
playlist = Playlist("MY MIX")
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")
print(len(playlist))

###__add__ the + operator makes you robject work with +
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1+v2
print(v3)

###__eq__ the = operator makes your object work with ==
class Student: 
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __eq__(self, other):
        return self.grade == other.grade
    
s1= Student("Carlos", 95)
s2= Student("Maria", 95)
s3= Student("Ana", 87)

print(s1==s2)
print(s1==s3)

###__lt__, __gt__ comparison operators makes your object work with < and >
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __lt__(self,other):
        return self.grade < other.grade
    def __gt__(self,other):
        return self.grade > other.grade
    def __str__(self):
        return f"{self.name} : {self.grade}"
    
s1 = Student("Carlos", 95)
s2 = Student("Maria", 87)
print(s1 > s2)
print(s2 < s1)

students = [
    Student("Carlos", 95),
    Student("Maria", 87),
    Student("Ana", 92)
]
ranked =sorted(students)
for s in ranked:
    print(s)

###__contains__ the in operator makes your object work with in
class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def __contains__(self,song):
        return song in self.songs
playlist = Playlist()
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Hotel California")

print("Hotel California" in playlist)
print("Stairway to Heaven" in playlist)

###__getitem__ the [] operator makes your object work with square brackets like a list
class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def __getitem__(self, index):
        return self. songs[index]
    def __len__(self):
        return len(self.songs)
playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")
print(playlist[0])
print(playlist[2])


####PUTTING ALL THE MOST IMPORTANT METHOS TOGETHER
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
    def __len__(self):
        return len(self.items)
    def __str__(self):
        total = sum(i["price"] for i in self.items)
        return f"Cart: {len(self)} items, total ${total:.2f}"
    def __contains__(self, item_name):
        return any(i["item"] == item_name for i in self.items)
    def __getitem__(self, index):
        return self.items[index]
    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        return new_cart
    
cart1= ShoppingCart()
cart1.add_item("Pizza", 12.99)
cart1.add_item("Soda", 2.50)

cart2 = ShoppingCart()
cart2.add_item("Burger", 8.99)

print(len(cart1))
print("Pizza" in cart1)
print(cart1[0])
print(cart1)

combined = cart1 + cart2
print(combined)