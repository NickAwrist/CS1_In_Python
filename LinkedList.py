# Linked List in Python by Nicholas Aristizabal

# Class for Node
class Node:
    # Its next Node and its data
    def __int__(self, data):
        self.data = data
        self.next = None

    # toString
    def __str__(self):
        return str(self.data)


# Function to create a new Node
def get_new_node() -> Node:
    new_node = Node()
    new_node.data = int(input("Enter data value for input: "))
    new_node.next = None
    return new_node


# Class for SinglyLinkedList
class LinkedList:
    # Head of the list
    def __init__(self):
        self.head = None

    # Method to add a node to the back of the list
    def add_to_back(self):
        # Create new node
        new_node = get_new_node()

        # Check if list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse through the list until we get to the last node
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next

        # Add new node to back of list
        temp_node.next = new_node

        return self.head

    # Method to add a node to the front of the list
    def add_to_front(self):
        new_node = get_new_node()

        if self.head is None:
            self.head = new_node
            return

        # Make new node front of list and re-assign the head
        new_node.next = self.head
        self.head = new_node

    # Method to add a node to a specific index starting at 0
    def add_to_index(self, index):
        new_node = get_new_node()

        if self.head is None:
            self.head = new_node
            return

        # If we are adding to the first index, add to front
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse until we get to the node that is before our desired index
        # and add the new node in front of it
        count = 0
        temp_node = self.head
        while count < index-1 and temp_node.next is not None:
            temp_node = temp_node.next
            count = count+1
        new_node.next = temp_node.next
        temp_node.next = new_node

    # Method to add a node sorted in increasing order
    def add_sorted(self):
        new_node = get_new_node()

        if self.head is None:
            self.head = new_node
            return

        # Check if new node's data is less than the head's data, if so, make new_node the first node
        if new_node.data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse until we get to the node before the one that is greater than the new node data
        temp_node = self.head
        while temp_node.next is not None and new_node.data > temp_node.next.data:
            temp_node = temp_node.next

        # Insert between the nodes that is <= and > our new node data
        new_node.next = temp_node.next
        temp_node.next = new_node

    # Method to delete a node from the back of the list
    def delete_from_back(self):
        if self.head is None:
            return
        # If head is the only node, delete it
        if self.head.next is None:
            self.head = None
            return

        # Traverse until we get to the second to last node and set its next to None
        temp_node = self.head
        while temp_node.next.next is not None:
            temp_node = temp_node.next

        temp_node.next = None

    # Method to delete a node from the front of the list
    def delete_from_front(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        # Delete the first node and reassign head
        self.head = self.head.next

    # Method to delete a node from a certain index in the list starting at 0
    def delete_from_index(self, index):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        if index == 0:
            self.head = self.head.next

        # Traverse until we reach node that is before desired index and add new node in front of it
        count = 0
        temp_node = self.head
        while count < index-1 and temp_node.next is not None:
            temp_node = temp_node.next
            count = count+1
        temp_node.next = temp_node.next.next

    # Method to print the list
    def print_list(self):
        # If list is empty print that it is empty
        if self.head is None:
            print("The linked list is empty")

        # Traverse entire list and print the data
        temp_node = self.head
        while temp_node:
            print(f"{temp_node} -> ", end="")
            temp_node = temp_node.next
        print("None")

    # Method to find a node with a certain value in the list
    def search(self, data) -> Node | None:
        # If list is empty, return None
        if self.head is None:
            print("List is empty")
            return None

        # Traverse the list until the end, or we find desired node with data
        temp_node = self.head
        while temp_node is not None and temp_node.data != data:
            temp_node = temp_node.next

        # Return the node, if we could not find the node, it will return None
        return temp_node


def print_menu():
    print("1. Add to front\n"
          "2. Add to an index\n"
          "3. Add to the back\n"
          "4. Add sorted\n"
          "5. Delete from the front\n"
          "6. Delete from an index\n"
          "7. Delete from the back\n"
          "8. Search for a value\n"
          "9. Print the list\n"
          "10. Exit\n")


list1 = LinkedList()

choice = 0

while choice != 10:

    print_menu()
    match int(input("Enter an option: ")):
        case 1:
            list1.add_to_front()
        case 2:
            list1.add_to_index(int(input(" Which index would you like to add to? 0 for first index")))
        case 3:
            list1.add_to_back()
        case 4:
            list1.add_sorted()
        case 5:
            list1.delete_from_front()
        case 6:
            list1.delete_from_index(int(input(" Which index would you like to delete from? 0 for first index")))
        case 7:
            list1.delete_from_back()
        case 8:
            search_node = list1.search(int(input("What value do you want to search for?")))
            if search_node:
                print(f"Found node with data {search_node.data}")
            else:
                print(f"Could not find node")
        case 9:
            list1.print_list()
        case 10:
            choice = 10
            print("Thank you!")
        case _:
            print("Error, choose an option from 1-10")
