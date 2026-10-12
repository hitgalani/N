# ========================================================================
# VERSION 1 — STACK
# ========================================================================
def main():
    stack = []

    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter element: ")
            stack.append(item)
            print("Element inserted:", item)
        elif choice == 2:
            if not stack:
                print("Stack is empty.")
            else:
                print("Deleted element:", stack.pop())
        elif choice == 3:
            print("Stack elements:", stack)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

# ===========================simple stack implementation using class===========================

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(self.items)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)


o = Stack()

o.push(1)
o.push(2)
o.push(3)
o.push(4)

print(o.pop())
print(o.peek())
print(o.size())

# ===========================simple stack implementation using class and while loop and input===========================
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(self.items)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

o = Stack()
while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        item = input("Enter element: ")
        o.push(item)
    elif choice == 2:
        print("Deleted element:", o.pop())
    elif choice == 3:
        print("Top element:", o.peek())
    elif choice == 4:
        print("Stack size:", o.size())
    elif choice == 5:
        break
    else:
        print("Invalid choice.")


# ========================================================================
# VERSION 2 — QUEUE
# ========================================================================
from collections import deque

def main():
    queue = deque()

    while True:
        print("\n--- QUEUE MENU ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter element: ")
            queue.append(item)
            print("Element inserted:", item)
        elif choice == 2:
            if not queue:
                print("Queue is empty.")
            else:
                print("Deleted element:", queue.popleft())
        elif choice == 3:
            print("Queue elements:", list(queue))
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

# ===========================queue implementation using class===========================
class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(self.items)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def size(self):
        return len(self.items)
o = Queue()
o.enqueue(1)
o.enqueue(2)
o.enqueue(3)
o.enqueue(4)

print(o.dequeue())
print(o.peek())
print(o.size())

# ===========================simple stack implementation using class and while loop and input===========================
class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(self.items)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def size(self):
        return len(self.items)
o = Queue()
while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        item = input("Enter element: ")
        o.enqueue(item)
    elif choice == 2:
        print("Deleted element:", o.dequeue())
    elif choice == 3:
        print("Front element:", o.peek())
    elif choice == 4:
        print("Queue size:", o.size())
    elif choice == 5:
        break
    else:
        print("Invalid choice.")

# ===========================Infix to postfix conversion===========================

# Infix to Postfix Conversion

def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0


def infix_to_postfix(expression):
    stack = []
    postfix = []

    for char in expression:
        if char == ' ':
            continue

        # If operand, add it to postfix
        if char.isalnum():
            postfix.append(char)

        # If opening bracket, push onto stack
        elif char == '(':
            stack.append(char)

        # If closing bracket, pop until opening bracket
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            if stack:
                stack.pop()

        # If operator, handle precedence
        else:
            while stack and stack[-1] != '(' and (
                precedence(stack[-1]) > precedence(char)
                or (
                    precedence(stack[-1]) == precedence(char)
                    and char != '^'
                )
            ):
                postfix.append(stack.pop())

            stack.append(char)

    # Pop remaining operators
    while stack:
        if stack[-1] == '(':
            raise ValueError("Invalid expression: unmatched bracket")
        postfix.append(stack.pop())

    return ' '.join(postfix)


# Main program
infix_expression = "a+b*(c-d)/e"

postfix_expression = infix_to_postfix(infix_expression)

print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)


# ===========================Postfix to Infix Conversion===========================

def is_operand(char):
    return char.isalnum()


def postfix_to_infix(postfix_expression):
    stack = []

    for char in postfix_expression:
        if char == ' ':
            continue

        # If operand, push onto stack
        if is_operand(char):
            stack.append(char)

        # If operator, pop two operands
        elif char in '+-*/^':
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")

            operand2 = stack.pop()
            operand1 = stack.pop()

            # Create infix expression
            new_expression = (
                "(" + operand1 + " " + char + " " + operand2 + ")"
            )

            stack.append(new_expression)

        else:
            raise ValueError("Invalid character in expression")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack.pop()


# Main program
postfix_expression = "abc+*d/"

infix_expression = postfix_to_infix(postfix_expression)

print("Postfix Expression:", postfix_expression)
print("Infix Expression:", infix_expression)

