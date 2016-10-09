'''
Name: Yan Shi 
Updated: 11/30/2015 
Time Taken: 1 hour ? 
Discussed w/: N/A 
Question 1 

10 pts. For this exercise, you will be coding your very first 
class, a Queue class. Queues are a fundamental computer science
data structure. A queue is basically like a line at Disneyland--
you can add elements to a queue, and they maintain a specific order.
When you want to get something off the end of a queue, 
you get the items that has been in there the longest.
First in, first out (FIFO).''' 

class Queue: 
	def __init__(self): 
		self.elements = [] #initialize the list 

	def qinsert(self, element): 
		self.elements.insert(0, element) #appends elements to queue 
		print "Inserted " + str(element) + " into queue." # prints the statment that item has been inserted

	def qremove(self): 
		if len(self.elements)!=0: #checks to see if the length of the list is 0 
			return self.elements.pop() #if the length of the list != 0, return number 

		else: 
			return "There are no elements in the queue." #if the length of is the list == 0, return this

if __name__ == "__main__": 
	queue = Queue() 

	queue.qinsert(5)
	queue.qinsert(9)
	queue.qinsert(10)
	print "Removed from queue: " + str(queue.qremove())
	print "Removed from queue: " + str(queue.qremove())
	print "Removed from queue: " + str(queue.qremove())	






