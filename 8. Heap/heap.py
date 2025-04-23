"""
Filename: heap.py
Desription: Creates and manages MaxHeap and MinHeap
Author: Priyankar Shivhare
Date: April 23, 2025
"""

class MaxHeap():
    """Instantiate and Manages a Max Heap"""
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        """Inserts a new Node in the heap"""
        self.heap.append(value)
        current_node = len(self.heap) - 1
        while current_node > 0 and self.heap[self._parent(current_node)] < self.heap[current_node]:
            self._swap(self._parent(current_node),current_node)
            current_node = self._parent(current_node)

    def _sink_down(self, curr_index):
        """Sink down the node"""
        max_index = curr_index
        while curr_index < len(self.heap) - 1:
            if (self._left_child(curr_index) < len(self.heap) and
                self.heap[max_index] < self.heap[self._left_child(curr_index)]):
                max_index = self._left_child(curr_index)
            if (self._right_child(curr_index) < len(self.heap) and
                self.heap[max_index] < self.heap[self._right_child(curr_index)]):
                max_index = self._right_child(curr_index)
            if curr_index != max_index:
                self._swap(max_index, curr_index)
                curr_index = max_index
            else:
                break

    def remove(self):
        """Removes the top of the heap"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

class MinHeap():
    """Instantiate and Manages a Min Heap"""
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        """Inserts a new Node in the heap"""
        self.heap.append(value)
        current_node = len(self.heap) - 1
        while current_node > 0 and self.heap[self._parent(current_node)] > self.heap[current_node]:
            self._swap(self._parent(current_node),current_node)
            current_node = self._parent(current_node)

    def _sink_down(self, curr_index):
        """Sink down the node"""
        max_index = curr_index
        while curr_index < len(self.heap) - 1:
            if (self._left_child(curr_index) < len(self.heap) and
                self.heap[max_index] > self.heap[self._left_child(curr_index)]):
                max_index = self._left_child(curr_index)
            if (self._right_child(curr_index) < len(self.heap) and
                self.heap[max_index] > self.heap[self._right_child(curr_index)]):
                max_index = self._right_child(curr_index)
            if curr_index != max_index:
                self._swap(max_index, curr_index)
                curr_index = max_index
            else:
                break

    def remove(self):
        """Removes the top of the heap"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
