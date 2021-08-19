"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        root = self.head
        if self.head:
            while root.next:
                root = root.next
            root.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        count = 1
        root = self.head
        while root:
            if count == position:
                return root
            root = root.next
            count+=1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        count = 1
        root = self.head
        if position == 1:
            new_element.next = self.head
        else:
            while root:
                if count == position-1:
                    new_element.next = root.next
                    root.next = new_element
                root = root.next
                count +=1
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        root = self.head
        past = None
        while root.value != value and root.next:
            past = root
            root = root.next
        if root.value == value:
            if past:
                past.next = root.next
            else:
                self.head = root.next
        
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
e4 = Element(4)
ll.insert(e4,3)
print(ll.get_position(3).value)
ll.delete(1)
print(ll.get_position(2).value)
# ll.delete(3)
print(ll.get_position(3).value)