from collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:

    if taxis[-1] >= customers[0]:
        total_time += customers.popleft()
    taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
