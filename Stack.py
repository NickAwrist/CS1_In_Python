# Stack in Python by Nicholas Aristizabal

# Class for node
class Node:
    def __int__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self) -> str:
        return "Name: "+self.name+" Data: "+str(self.data)


# Create a new node function
def get_new_node() -> Node:
    new_node = Node()
    new_node.name = input("Enter data value for name: ")
    new_node.data = int(input("Enter data value for data: "))
    return new_node


# Class for stack
class Stack:
    def __init__(self, size: int):
        self.arr = [] * size
        self.top = -1
        self.size = size

    # Method to check if stack is empty
    def is_empty(self) -> bool:
        return self.top == -1

    # Method to check if stack is full
    def is_full(self) -> bool:
        return self.top == self.size - 1

    # Method to push a value to the stack
    def push(self):
        new_node = get_new_node()
        if self.is_full():
            print("Stack is full")
            return
        self.top = self.top + 1
        self.arr.append(new_node)

    # Method to pop a value from the stack
    def pop(self) -> Node | None:
        if self.is_empty():
            print("Stack is empty")
            return None
        self.top = self.top - 1
        return self.arr.pop()

    # Method to peek from the stack
    def peek(self) -> Node | None:
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.arr[self.top]

    # Method to print the stack
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
            return

        for i in range(self.top+1, 0, -1):
            print(f"|\t{self.arr[i-1]}\t|")
        print()


def print_menu():
    print("\n1. Push onto stack\n"
          "2. Pop from stack\n"
          "3. Peek in stack\n"
          "4. Print stack\n"
          "5. Exit\n")


s = Stack(10)

count = 0
while count != 5:
    print_menu()

    match(int(input("Enter an option between 1-5\n"))):
        case 1:
            s.push()
            peek_node = s.peek()
            print(f"Added {peek_node} to the stack")
        case 2:
            pop_node = s.pop()
            print(f"Popped {pop_node} from the stack")
        case 3:
            peek_node = s.peek()
            print(peek_node)
        case 4:
            s.print_stack()
        case 5:
            count = 5
        case _:
            print("Error, choose an option between 1-5\n")
