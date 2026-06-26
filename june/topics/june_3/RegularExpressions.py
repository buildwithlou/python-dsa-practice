# Regular Expressions (Regex; import re)
# Without regex
def is_valid_email(email):
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if email.count("@") != 1:
        return False
    # and 20 more checks...


# import re
# re.match()      #check pattern at the beginning of string
# re.search()     #find pattern ANYWHERE in string
# re.findall()    #find all matches, return as list
# re.sub()        #find and REPLACE matches

import re

# re.search - returns a match object if found, None if not
result = re.search("hello", "goodbye world")
print(bool(result))

# Special Characters
# . (any single character)
re.search("h.llo", "hello")
re.search("h.llo", "hallo")
re.search("h.llo", "hllo")  # needs exactly one character instead of .

# * (0 or more of previous)
re.search("ho*", "h")
re.search("ho*", "ho")
re.search("ho*", "hooo")

# + (1 or more of previous)
re.search("ho+", "h")  # needs at least one o
re.search("ho+", "ho")
re.search("ho+", "hooo")

# ? (0 or 1 of previous)
re.search("colou?r", "color")
re.search("colou?r", "colour")

# ^ (start of string)
re.search("^Hello", "Hello world")
re.search("^Hello", "Say Hello")  # needs to start with Hello

# $ (end of string)
re.search("world$", "hello world")
re.search("world$", "world peace")  # needs to end with world

# [abc] — matches a, b, or c
re.search("[aeiou]", "hello")

# [a-z] — any lowercase letter
re.search("[a-z]+", "hello")

# [A-Z] — any uppercase letter
re.search("[A-Z]+", "Hello")

# [0-9] — any digit
re.search("[0-9]+", "abc123")

# [^abc] — anything EXCEPT a, b, c
re.search("[^0-9]+", "hello123")

# \d   # any digit          = [0-9]
# \w   # any word character = [a-zA-Z0-9_]
# \s   # any whitespace     = space, tab, newline
# \D   # NOT a digit
# \W   # NOT a word character
# \S   # NOT whitespace
# \d{3}     # exactly 3 digits
# \d{3,}    # 3 or more digits
# \d{3,5}   # between 3 and 5 digits
# \w{4}     # exactly 4 word characters
# [a-z]{2,4} # 2 to 4 lowercase letters

re.search("\d+", "abc123")  # matches '123'
re.search("\w+", "hello world")  # matches 'hello'
re.search("\s+", "hello world")  # matches the space

# re.match (beginning of string only)
re.match("hello", "hello world")
re.match("world", "hello world")

# re.findall (returns all matches as list)
text = "My number is 123 and her number is 456"
numbers = re.findall("\d+", text)
print(numbers)  # ['123', '456']

words = re.findall("\w+", "hello world foo")
print(words)  # ['hello', 'world', 'foo']

# re.sub (find and replace)
text = "Hello World"
result = re.sub("World", "Carlos", text)
print(result)  # Hello Carlos

# Remove all digits
text = "abc123def456"
result = re.sub("\d+", "", text)
print(result)  # abcdef

# Replace whitespace with underscore
text = "hello world foo"
result = re.sub("\s+", "_", text)
print(result)  # hello_world_foo


###Real World Use Cases
# validate email
def is_valid_email(email):
    pattern = r"\w+@\w+\.\w+"
    return bool(re.match(pattern, email))


print(is_valid_email("carlos@gmail.com"))
print(is_valid_email("notanemail"))
print(is_valid_email("missing@dot"))


# validate phone number
def is_valid_phone(phone):
    pattern = r"\d{10}"
    return bool(re.match(pattern, phone))


print(is_valid_phone("1234567890"))
print(is_valid_phone("123456"))

# Extract all emails from text
text = "Contact us at carlos@gmail.com or support@company.com for help"
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)

# Clean up user Input
user_input = "     Hello        World     "
clean = re.sub("\s+", " ", user_input).strip()
print(clean)
