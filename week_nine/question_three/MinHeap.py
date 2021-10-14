class MinHeap:
    # Initializing the init function of the min heap class
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * self.maxsize
        self.FRONT = 1

    # Below i will be creating the functions that i will use to properly implement my min-heap
    # Creating the function that will return the position of the parent node
    def parent(self, pos):
        return pos // 2

    # Creating the function that will return the position of the left node
    def left_Child(self, pos):
        return 2 * pos

    # Creating the function that will return the position of the right node
    def right_Child(self, pos):
        return (2 * pos) + 1

    # Function to check if the node passed is a leaf
    def leaf(self, pos):
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    # Function to swap nodes in the leaf
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to create the heap
    def min_heap(self, pos):
        # For when the node is greater than its children and it is not a leaf
        if not self.leaf(pos):
            if (self.Heap[pos] > self.Heap[self.left_Child(pos)] or
                    self.Heap[pos] > self.Heap[self.right_Child(pos)]):

                # Heapify with the left child
                if self.Heap[self.left_Child(pos)] < self.Heap[self.right_Child(pos)]:
                    self.swap(pos, self.left_Child(pos))
                    self.min_heap(self.left_Child(pos))

                    # Heapify with the right child
                else:
                    self.swap(pos, self.right_Child(pos))
                    self.min_heap(self.right_Child(pos))

    # Below i will be creating my methods for the min heap class
    # Function to insert into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

        return element

    # Function to print the contents of my heap
    def print(self):
        for i in range(1, (self.size // 2) + 1):
            x = "Parent: " + str(self.Heap[i]) + " Left: " + str(self.Heap[2 * i]) + " Right: " + str(
                self.Heap[2 * i + 1])
            return x

    # Function to find the lowest value in the heap
    def min_value(self):

        for pos in range(self.size // 2, 0, -1):
            self.min_heap(pos)

    # Function to delete the lowest value from the heap
    def delete_min_value(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.min_heap(self.FRONT)
        return popped
