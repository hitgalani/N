"""
BEGINNER PYTHON PRACTICALS — SEPARATE VERSIONS IN ONE FILE

How to run:
  python beginner_practicals.py 1    # Stack
  python beginner_practicals.py 2    # Queue
  ...
  python beginner_practicals.py 11   # Binary Search Tree

Run only one version at a time. Each section below is a complete,
independent program and follows the supplied material's single-character
expression examples and beginner-level data-structure operations.

Versions:
  1 Stack
  2 Queue
  3 Infix to Postfix
  4 Postfix to Infix
  5 Infix to Prefix
  6 Prefix to Infix
  7 Deque
  8 Bubble Sort
  9 Selection Sort
 10 Quick Sort
 11 Binary Search Tree (inorder traversal)
"""


# ========================================================================
# VERSION 1 — STACK
# ========================================================================
VERSION_1_CODE = r"""def main():
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

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 2 — QUEUE
# ========================================================================
VERSION_2_CODE = r"""from collections import deque

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

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 3 — INFIX TO POSTFIX
# ========================================================================
VERSION_3_CODE = r"""OPERATORS = "+-*/^"

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
            while (stack and stack[-1] != "(" and
                   (precedence(stack[-1]) > precedence(char) or
                    (precedence(stack[-1]) == precedence(char) and char != "^"))):
                output.append(stack.pop())
            stack.append(char)
        else:
            return "Invalid character"

    if "(" in stack:
        return "Invalid expression"

    while stack:
        output.append(stack.pop())

    return "".join(output)

def main():
    expression = input("Enter infix expression (e.g. A+B*C): ")
    print("Postfix expression:", infix_to_postfix(expression))

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 4 — POSTFIX TO INFIX
# ========================================================================
VERSION_4_CODE = r"""OPERATORS = "+-*/^"

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

def main():
    expression = input("Enter postfix expression (e.g. AB+C*): ")
    print("Infix expression:", postfix_to_infix(expression))

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 5 — INFIX TO PREFIX
# ========================================================================
VERSION_5_CODE = r"""OPERATORS = "+-*/^"

def precedence(operator):
    if operator in ("+", "-"):
        return 1
    if operator in ("*", "/"):
        return 2
    if operator == "^":
        return 3
    return 0

def infix_to_prefix(expression):
    expression = expression.replace(" ", "")
    expression = expression[::-1].replace("(", "#").replace(")", "(").replace("#", ")")
    stack = []
    output = []

    for char in expression:
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
            while (stack and stack[-1] != "(" and
                   (precedence(stack[-1]) > precedence(char) or
                    (precedence(stack[-1]) == precedence(char) and char == "^"))):
                output.append(stack.pop())
            stack.append(char)
        else:
            return "Invalid character"

    if "(" in stack:
        return "Invalid expression"

    while stack:
        output.append(stack.pop())

    return "".join(output[::-1])

def main():
    expression = input("Enter infix expression (e.g. A+B*C): ")
    print("Prefix expression:", infix_to_prefix(expression))

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 6 — PREFIX TO INFIX
# ========================================================================
VERSION_6_CODE = r"""OPERATORS = "+-*/^"

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

def main():
    expression = input("Enter prefix expression (e.g. +A*BC): ")
    print("Infix expression:", prefix_to_infix(expression))

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 7 — DEQUE
# ========================================================================
VERSION_7_CODE = r"""from collections import deque

def main():
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

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 8 — BUBBLE SORT
# ========================================================================
VERSION_8_CODE = r"""def bubble_sort(numbers):
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

def main():
    try:
        numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
    except ValueError:
        print("Please enter integers only.")
        return
    print("Sorted list:", bubble_sort(numbers))

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 9 — SELECTION SORT
# ========================================================================
VERSION_9_CODE = r"""def selection_sort(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers

def main():
    try:
        numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
    except ValueError:
        print("Please enter integers only.")
        return
    print("Sorted list:", selection_sort(numbers))

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 10 — QUICK SORT
# ========================================================================
VERSION_10_CODE = r"""def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()

    pivot = numbers[len(numbers) // 2]
    smaller = [value for value in numbers if value < pivot]
    equal = [value for value in numbers if value == pivot]
    larger = [value for value in numbers if value > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)

def main():
    try:
        numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
    except ValueError:
        print("Please enter integers only.")
        return
    print("Sorted list:", quick_sort(numbers))

if __name__ == "__main__":
    main()"""

# ========================================================================
# VERSION 11 — BINARY SEARCH TREE (INORDER)
# ========================================================================
VERSION_11_CODE = r"""class Node:
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

def main():
    try:
        numbers = [int(value) for value in input("Enter BST values separated by spaces: ").split()]
    except ValueError:
        print("Please enter integers only.")
        return

    root = None
    for number in numbers:
        root = insert(root, number)

    print("BST inorder traversal (sorted order):")
    inorder(root)
    print()

if __name__ == "__main__":
    main()"""


def main():
    import sys

    versions = {
        "1": ("Stack", VERSION_1_CODE),
        "2": ("Queue", VERSION_2_CODE),
        "3": ("Infix to Postfix", VERSION_3_CODE),
        "4": ("Postfix to Infix", VERSION_4_CODE),
        "5": ("Infix to Prefix", VERSION_5_CODE),
        "6": ("Prefix to Infix", VERSION_6_CODE),
        "7": ("Deque", VERSION_7_CODE),
        "8": ("Bubble Sort", VERSION_8_CODE),
        "9": ("Selection Sort", VERSION_9_CODE),
        "10": ("Quick Sort", VERSION_10_CODE),
        "11": ("Binary Search Tree", VERSION_11_CODE),
    }

    if len(sys.argv) != 2 or sys.argv[1] not in versions:
        print("Choose one version by number:")
        for number, (name, _) in versions.items():
            print(f"{number}. {name}")
        print("\nExample: python beginner_practicals.py 1")
        return

    name, code = versions[sys.argv[1]]
    print(f"Running Version {sys.argv[1]}: {name}")
    namespace = {"__name__": "__main__"}
    exec(compile(code, f"<Version {sys.argv[1]}: {name}>", "exec"), namespace)

if __name__ == "__main__":
    main()
