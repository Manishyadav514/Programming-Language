# FOLLOWS LIFO POLICY
import queue
q = queue.Queue(5)
for i in range(5):
    q.put(i) # enqueue element in queue, This will put the item inside the queue.
print(q.empty())  # It will return true if the queue is empty and false if items are present.
print(q.qsize())  # returns the size of the queue.
print(q.full()) # will return true.
while not q.empty():
    print("FIFO", q.get())   # This will return you an item from the queue.

# FOLLOWS FIFO POLICY
import queue
q = queue.LifoQueue()
for _ in range(5):
    q.put(input().split())
while not q.empty():
    print("LIFO", q.get())
