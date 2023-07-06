#lists
a=[]
a.append(10)
a.append(5)
a.sort(reverse=False)
print(a.pop(0))


#using heapq
import heapq
qu=[]
heapq.heappush(qu,(1,200903))
heapq.heappush(qu,(2,70))
heapq.heappush(qu,(4,2903))
heapq.heappush(qu,(3,20003))
while qu:
    print(heapq.heappop(qu))


#using queue
import queue
q=queue.PriorityQueue()
q.put(10)
q.put(30)
q.put(20)
q.put(40)
q.put(70)
print(q.get())
print(q.get())


#using tuple(we are giving priority and then by sorting we will pop the elements)
q=[]
q.append((1,"alexa"))
q.append((5,"rexona"))
q.append((3,"harry"))
q.append((2,"tom"))
q.append((4,"jerry"))
q.sort()
print(q.pop(0))
print(q.pop(0))
