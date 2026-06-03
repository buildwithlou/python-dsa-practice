#Challenge: Extract all valid emails for the next list and extract all phone numbers with format (###-###-####)
import re
data = [
    "carlos@gmail.com",
    "notanemail",
    "maria@yahoo.com",
    "12345",
    "ana@company.org",
    "invalid@",
    "305-123-4567",
    "bob@outlook.com"
]

emails = r"\w+@\w+\.\w+"
phone_number = r"^\d{3}-\d{3}-\d{4}"
new_emails = []
new_phone_numbers = []
for line in data:
    if re.match(emails,line):
        new_emails.append(line)
    elif re.match(phone_number,line):
        new_phone_numbers.append(line)

print("Emails: ", new_emails)
print("Phone Numbers: " ,new_phone_numbers)

