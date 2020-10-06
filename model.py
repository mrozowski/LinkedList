

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.size += 1

    def sort_asc(self):
        """Bubble sort"""
        for i in range(self.size):
            prev = self.head
            current = self.head.next
            while current:
                if prev.val > current.val:
                    temp = prev.val
                    prev.val = current.val
                    current.val = temp
                prev = current
                current = current.next

    def sort_desc(self):
        """Initiate Merge sort - This method is called from presenter"""
        if self.head is None: return
        self.head = self.merge_sort(self.head)
        """Set the new tail"""
        current = self.head
        while current.next:
            current = current.next
        self.tail = current

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_middle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.merge_sort(head)

        # Apply mergeSort on right list
        right = self.merge_sort(next_middle)

        # Merge the left and right lists
        sortedlist = self.sorted_merge(left, right)
        return sortedlist

    def get_middle(self, head):
        if head is None:
            return head

        current = head
        double = head

        """When double reach the end of list current will be exactly in the middle"""
        while double.next is not None and double.next.next is not None:
            current = current.next
            double = double.next.next
        return current

    def sorted_merge(self, left, right):
        result = None

        if left is None:
            return right
        if right is None:
            return left

        if left.val >= right.val:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)

        return result

    def remove_duplicates(self):
        if self.size < 2:
            return
        i = 1
        temp = [self.head.val]
        current = self.head.next
        while current:
            if temp.__contains__(current.val):  # if there is such element already then delete it
                current = current.next
                self.remove(i)
            else:
                temp.append(current.val)
                current = current.next
                i += 1

    def remove(self, p):
        if p < self.size:
            if p == 0:
                self.head = self.head.next
                self.size -= 1
                return
            i = 1
            current = self.head.next  # we start from second node
            prev = self.head
            while current:
                if i == p:
                    prev.next = current.next
                    if p == self.size - 1:
                        self.tail = prev
                    self.size -= 1
                    return
                prev = current
                current = current.next
                i += 1

    def reverse(self):
        current = self.head
        prev = None
        while current:
            _next = current.next
            current.next = prev
            prev = current
            current = _next

        self.tail = self.head
        self.head = prev

    def get_values(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

    def to_string(self):
        string = ""
        current = self.head
        while current:
            string += str(current.val) + " | "
            current = current.next

        return string


class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


