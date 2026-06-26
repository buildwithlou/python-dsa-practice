#####Stack (LIFO - Last In, First Out) (Push(Append) and Pop)
stack = []

# Push — add to top
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  # [10, 20, 30]

# Pop — remove from top
stack.pop()
print(stack)  # [10, 20]

# Peek — see what's on top without removing
print(stack[-1])  # 20

# Check if empty
print(len(stack) == 0)  # False

#####Queue (FIFO - First In, First Out) (Enqueue(Append) and Dequeue(Pop from front))
from collections import deque

queue = deque()
queue.append("Carlos")
queue.append("Maria")
queue.append("Ana")
print(queue)  # deque(['Carlos', 'Maria', 'Ana'])

# Dequeue — remove from front
queue.popleft()
print(queue)  # deque(['Maria', 'Ana'])

# Peek at front
print(queue[0])  # Maria

# Check if empty
print(len(queue) == 0)  # False

#####Heap (Min-Heap or Max-Heap) (heapify, heappush, heappop)
import heapq

numbers = [30, 10, 50, 20, 40]

# Turn list into a heap
heapq.heapify(numbers)
print(numbers)  # [10, 20, 50, 30, 40] — 10 is always at top

# Add a number
heapq.heappush(numbers, 5)
print(numbers)  # [5, 20, 10, 30, 40, 50] — 5 is now at top

# Remove the smallest (the top)
smallest = heapq.heappop(numbers)
print(smallest)  # 5
print(numbers)  # [10, 20, 50, 30, 40] — 10 back on top
