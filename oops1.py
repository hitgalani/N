from collections import deque


# 1. STACK USING LIST

def stack_menu():
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
            if stack:
                print("Deleted element:", stack.pop())
            else:
                print("Stack is empty.")
        elif choice == 3:
            print("Stack elements:", stack)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")


# 2. STACK USING CLASS

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

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


def stack_class_demo():
    obj = Stack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)

    print("Stack:", obj.items)
    print("Pop:", obj.pop())
    print("Peek:", obj.peek())
    print("Size:", obj.size())


# 3. STACK USING CLASS AND WHILE LOOP

def stack_class_menu():
    obj = Stack()

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
            obj.push(input("Enter element: "))
            print("Stack:", obj.items)
        elif choice == 2:
            print("Deleted element:", obj.pop())
        elif choice == 3:
            print("Top element:", obj.peek())
        elif choice == 4:
            print("Stack size:", obj.size())
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


# 4. QUEUE USING DEQUE

def queue_menu():
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
            if queue:
                print("Deleted element:", queue.popleft())
            else:
                print("Queue is empty.")
        elif choice == 3:
            print("Queue elements:", list(queue))
        elif choice == 4:
            break
        else:
            print("Invalid choice.")


# 5. QUEUE USING CLASS

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

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


def queue_class_demo():
    obj = Queue()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)

    print("Queue:", list(obj.items))
    print("Dequeue:", obj.dequeue())
    print("Peek:", obj.peek())
    print("Size:", obj.size())


# 6. QUEUE USING CLASS AND WHILE LOOP

def queue_class_menu():
    obj = Queue()

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
            obj.enqueue(input("Enter element: "))
            print("Queue:", list(obj.items))
        elif choice == 2:
            print("Deleted element:", obj.dequeue())
        elif choice == 3:
            print("Front element:", obj.peek())
        elif choice == 4:
            print("Queue size:", obj.size())
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


# 7. INFIX TO POSTFIX

OPERATORS = "+-*/^"


def precedence(operator):
    if operator in ("+", "-"):
        return 1
    if operator in ("*", "/"):
        return 2
    if operator == "^":
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    for char in expression.replace(" ", ""):
        if char.isalnum():
            output.append(char)

        elif char == "(":
            stack.append(char)

        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            if not stack:
                return "Invalid expression"

            stack.pop()

        elif char in OPERATORS:
            while stack and stack[-1] != "(":
                top = stack[-1]

                if (precedence(top) > precedence(char) or
                    (precedence(top) == precedence(char)
                     and char != "^")):
                    output.append(stack.pop())
                else:
                    break

            stack.append(char)

        else:
            return "Invalid character"

    if "(" in stack:
        return "Invalid expression"

    while stack:
        output.append(stack.pop())

    return "".join(output)


def infix_postfix_demo():
    expression = input("Enter infix expression (e.g. A+B*C): ")
    print("Postfix expression:", infix_to_postfix(expression))


# 8. POSTFIX TO INFIX

def postfix_to_infix(expression):
    stack = []

    for char in expression.replace(" ", ""):
        if char.isalnum():
            stack.append(char)

        elif char in OPERATORS:
            if len(stack) < 2:
                return "Invalid postfix expression"

            right = stack.pop()
            left = stack.pop()
            stack.append("(" + left + char + right + ")")

        else:
            return "Invalid character"

    if len(stack) != 1:
        return "Invalid postfix expression"

    return stack.pop()


def postfix_infix_demo():
    expression = input("Enter postfix expression (e.g. AB+C*): ")
    print("Infix expression:", postfix_to_infix(expression))


# 9. INFIX TO PREFIX

def infix_to_prefix(expression):
    expression = expression.replace(" ", "")

    reversed_expression = (
        expression[::-1]
        .replace("(", "#")
        .replace(")", "(")
        .replace("#", ")")
    )

    stack = []
    output = []

    for char in reversed_expression:
        if char.isalnum():
            output.append(char)

        elif char == "(":
            stack.append(char)

        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            if not stack:
                return "Invalid expression"

            stack.pop()

        elif char in OPERATORS:
            while stack and stack[-1] != "(":
                top = stack[-1]

                if (precedence(top) > precedence(char) or
                    (precedence(top) == precedence(char)
                     and char == "^")):
                    output.append(stack.pop())
                else:
                    break

            stack.append(char)

        else:
            return "Invalid character"

    if "(" in stack:
        return "Invalid expression"

    while stack:
        output.append(stack.pop())

    return "".join(output[::-1])


def infix_prefix_demo():
    expression = input("Enter infix expression (e.g. A+B*C): ")
    print("Prefix expression:", infix_to_prefix(expression))


# 10. PREFIX TO INFIX

def prefix_to_infix(expression):
    stack = []

    for char in expression.replace(" ", "")[::-1]:
        if char.isalnum():
            stack.append(char)

        elif char in OPERATORS:
            if len(stack) < 2:
                return "Invalid prefix expression"

            left = stack.pop()
            right = stack.pop()
            stack.append("(" + left + char + right + ")")

        else:
            return "Invalid character"

    if len(stack) != 1:
        return "Invalid prefix expression"

    return stack.pop()


def prefix_infix_demo():
    expression = input("Enter prefix expression (e.g. +A*BC): ")
    print("Infix expression:", prefix_to_infix(expression))


# 11. DEQUE

def deque_menu():
    items = deque()

    while True:
        print("\n--- DEQUE MENU ---")
        print("1. Insert at front")
        print("2. Insert at rear")
        print("3. Delete from front")
        print("4. Delete from rear")
        print("5. Display")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter element: ")
            items.appendleft(item)
            print("Inserted:", item)
        elif choice == 2:
            item = input("Enter element: ")
            items.append(item)
            print("Inserted:", item)
        elif choice == 3:
            print("Deleted:", items.popleft() if items else "Deque is empty")
        elif choice == 4:
            print("Deleted:", items.pop() if items else "Deque is empty")
        elif choice == 5:
            print("Deque elements:", list(items))
        elif choice == 6:
            break
        else:
            print("Invalid choice.")


# 12. BUBBLE SORT

def bubble_sort(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers) - 1):
        swapped = False

        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


# 13. SELECTION SORT

def selection_sort(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers) - 1):
        min_index = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


# 14. QUICK SORT

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()

    pivot = numbers[len(numbers) // 2]

    smaller = [value for value in numbers if value < pivot]
    equal = [value for value in numbers if value == pivot]
    larger = [value for value in numbers if value > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


def sorting_demo():
    try:
        numbers = [
            int(value)
            for value in input("Enter integers separated by spaces: ").split()
        ]
    except ValueError:
        print("Please enter integers only.")
        return

    print("Bubble sort:", bubble_sort(numbers))
    print("Selection sort:", selection_sort(numbers))
    print("Quick sort:", quick_sort(numbers))


# 15. BINARY SEARCH TREE

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def bst_demo():
    try:
        numbers = [
            int(value)
            for value in input("Enter BST values separated by spaces: ").split()
        ]
    except ValueError:
        print("Please enter integers only.")
        return

    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST inorder traversal:")
    inorder(root)
    print()


# 16. STACK, QUEUE, SORTING, AND TREE PRACTICALS MENU

def main():
    while True:
        print("\n========== DATA STRUCTURES PRACTICALS ==========")
        print("1. Stack using list")
        print("2. Stack using class")
        print("3. Stack using class and while loop")
        print("4. Queue using deque")
        print("5. Queue using class")
        print("6. Queue using class and while loop")
        print("7. Infix to postfix")
        print("8. Postfix to infix")
        print("9. Infix to prefix")
        print("10. Prefix to infix")
        print("11. Deque")
        print("12. Bubble sort")
        print("13. Selection sort")
        print("14. Quick sort")
        print("15. Binary search tree")
        print("16. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            stack_menu()
        elif choice == 2:
            stack_class_demo()
        elif choice == 3:
            stack_class_menu()
        elif choice == 4:
            queue_menu()
        elif choice == 5:
            queue_class_demo()
        elif choice == 6:
            queue_class_menu()
        elif choice == 7:
            infix_postfix_demo()
        elif choice == 8:
            postfix_infix_demo()
        elif choice == 9:
            infix_prefix_demo()
        elif choice == 10:
            prefix_infix_demo()
        elif choice == 11:
            deque_menu()
        elif choice == 12:
            sorting_demo()
        elif choice == 13:
            sorting_demo()
        elif choice == 14:
            sorting_demo()
        elif choice == 15:
            bst_demo()
        elif choice == 16:
            print("Program ended.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()