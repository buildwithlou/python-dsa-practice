# 1. STACK
# You have a list of pages visited in a browser
# Simulate the back button being pressed 2 times
pages = []
pages.append("google.com")
pages.append("youtube.com")
pages.append("github.com")
print(pages)   # ['google.com', 'youtube.com', 'github.com']
# press back twice and print where you end up
pages.pop()
pages.pop()
print(pages)

# 2. QUEUE
# A printer has 3 jobs queued
# Process them one by one and print which job is being printed
from collections import deque
printer = deque()
printer.append("Document1.pdf")
printer.append("Photo.png")
printer.append("Report.docx")
print(printer)   # deque(['Document1.pdf', 'Photo.png', 'Report.docx'])
# process all jobs
while printer:
    document = printer.popleft()
    print(f"Printing {document}...")

# 3. HEAP
import heapq
# Find the 2 smallest numbers from this list using heapq
numbers = [40, 10, 30, 50, 20]
heapq.heapify(numbers)  # turn list into a heap
smallest = heapq.heappop(numbers)  # remove and return smallest
second_smallest = heapq.heappop(numbers)  # remove and return next smallest
print(smallest, second_smallest)  # 10 20