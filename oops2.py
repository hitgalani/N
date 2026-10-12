
# ============================================================
# OBJECT ORIENTED PROGRAMMING WITH PYTHON
# ALL 19 PRACTICALS IN ONE PYTHON PROGRAM
# ============================================================

from collections import deque


# ============================================================
# PRACTICAL 1: STUDENT CLASS
# ============================================================

def practical_1():
    class Student:
        def __init__(self, name, roll_no):
            self.name = name
            self.roll_no = roll_no

        def display(self):
            print("Name   :", self.name)
            print("Roll No:", self.roll_no)

    s1 = Student("Amit Sharma", 21)
    s1.display()


# ============================================================
# PRACTICAL 2: EMPLOYEE CLASS WITH getdata() AND putdata()
# ============================================================

def practical_2():
    class Employee:
        def getdata(self):
            self.name = input("Enter employee name: ")
            self.eid = int(input("Enter employee ID: "))
            self.salary = float(input("Enter employee salary: "))

        def putdata(self):
            print("\nEmployee Details")
            print("Name   :", self.name)
            print("ID     :", self.eid)
            print("Salary :", self.salary)

    e1 = Employee()
    e1.getdata()
    e1.putdata()


# ============================================================
# PRACTICAL 3: ACCOUNT AND SIMPLE INTEREST
# ============================================================

def practical_3():
    class Account:
        def __init__(self, acc_no, balance):
            self.acc_no = acc_no
            self.balance = balance

        def calculate_si(self, rate, time):
            si = (self.balance * rate * time) / 100
            print("Account No     :", self.acc_no)
            print("Principal      :", self.balance)
            print("Simple Interest:", si)
            print("Total Amount   :", self.balance + si)

    a1 = Account(1001, 50000)
    a1.calculate_si(rate=8, time=3)


# ============================================================
# PRACTICAL 4: STUDENT RESULT AND CLASS
# ============================================================

def practical_4():
    class Student:
        def __init__(self, rno, name, marks):
            self.rno = rno
            self.name = name
            self.marks = marks

        def result(self):
            total = sum(self.marks)
            percentage = total / len(self.marks)

            if percentage >= 75:
                grade = "Distinction"
            elif percentage >= 60:
                grade = "First Class"
            elif percentage >= 50:
                grade = "Second Class"
            elif percentage >= 40:
                grade = "Pass Class"
            else:
                grade = "Fail"

            print("Roll No   :", self.rno)
            print("Name      :", self.name)
            print("Total     :", total)
            print("Percentage:", percentage)
            print("Class     :", grade)

    s1 = Student(1, "Sneha Patil", [85, 78, 92, 88, 74])
    s1.result()


# ============================================================
# PRACTICAL 5: PERSON AND STUDENT INHERITANCE
# ============================================================

def practical_5():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def display_person(self):
            print("Name:", self.name)
            print("Age :", self.age)

    class Student(Person):
        def __init__(self, name, age, rno, course):
            super().__init__(name, age)
            self.rno = rno
            self.course = course

        def display_student(self):
            self.display_person()
            print("Roll No:", self.rno)
            print("Course :", self.course)

    s1 = Student("Kiran Joshi", 20, 15, "B.Sc Computer Science")
    s1.display_student()


# ============================================================
# PRACTICAL 6: MULTIPLE INHERITANCE AND CALCULATIONS
# ============================================================

def practical_6():
    class A:
        def __init__(self, no1):
            self.no1 = no1

    class B:
        def __init__(self, no2):
            self.no2 = no2

    class C(A, B):
        def __init__(self, no1, no2):
            A.__init__(self, no1)
            B.__init__(self, no2)

        def add(self):
            print("Addition       :", self.no1 + self.no2)

        def subtract(self):
            print("Subtraction    :", self.no1 - self.no2)

        def multiply(self):
            print("Multiplication :", self.no1 * self.no2)

        def divide(self):
            if self.no2 == 0:
                print("Division by zero is not possible.")
            else:
                print("Division       :", self.no1 / self.no2)

    c1 = C(20, 4)
    c1.add()
    c1.subtract()
    c1.multiply()
    c1.divide()


# ============================================================
# PRACTICAL 7: PERSON, EMPLOYEE AND PROGRAMMER INHERITANCE
# ============================================================

def practical_7():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Employee(Person):
        def __init__(self, name, age, eid, salary):
            super().__init__(name, age)
            self.eid = eid
            self.salary = salary

    class Programmer(Employee):
        def __init__(self, name, age, eid, salary, no_of_lang):
            super().__init__(name, age, eid, salary)
            self.no_of_lang = no_of_lang

        def show(self):
            print("Name           :", self.name)
            print("Age            :", self.age)
            print("Employee ID    :", self.eid)
            print("Salary         :", self.salary)
            print("Languages Known:", self.no_of_lang)

    p1 = Programmer("Aditya Rao", 27, 501, 65000, 4)
    p1.show()


# ============================================================
# PRACTICAL 8: CUSTOMER, DEPOSITOR AND BORROWER
# ============================================================

def practical_8():
    class Customer:
        def __init__(self, cid, name, phone_number):
            self.cid = cid
            self.name = name
            self.phone_number = phone_number

    class Depositor(Customer):
        def __init__(self, cid, name, phone_number, accno, balance):
            super().__init__(cid, name, phone_number)
            self.accno = accno
            self.balance = balance

    class Borrower(Depositor):
        def __init__(self, cid, name, phone_number, accno,
                     balance, loan_no, loan_amt):
            super().__init__(
                cid, name, phone_number, accno, balance
            )
            self.loan_no = loan_no
            self.loan_amt = loan_amt

        def display(self):
            print("Customer ID :", self.cid)
            print("Name         :", self.name)
            print("Phone Number :", self.phone_number)
            print("Account No   :", self.accno)
            print("Balance      :", self.balance)
            print("Loan No      :", self.loan_no)
            print("Loan Amount  :", self.loan_amt)

    b1 = Borrower(
        1, "Priya Deshmukh", "9876543210",
        2001, 75000, 501, 200000
    )
    b1.display()


# ============================================================
# PRACTICAL 9: STUDENT, MARKS, SPORTS AND RESULT
# ============================================================

def practical_9():
    class Student:
        def getStu(self, id, name):
            self.id = id
            self.name = name

    class Marks(Student):
        def getMarks(self, mark1, mark2, mark3):
            self.mark1 = mark1
            self.mark2 = mark2
            self.mark3 = mark3

    class Sports:
        def getSPMarks(self, spmarks):
            self.spmarks = spmarks

    class Result(Marks, Sports):
        def show_result(self):
            self.total = (
                self.mark1 + self.mark2
                + self.mark3 + self.spmarks
            )
            self.avg = self.total / 4

            print("ID      :", self.id)
            print("Name    :", self.name)
            print("Total   :", self.total)
            print("Average :", self.avg)

    r1 = Result()
    r1.getStu(10, "Neha Kulkarni")
    r1.getMarks(85, 90, 78)
    r1.getSPMarks(45)
    r1.show_result()


# ============================================================
# PRACTICAL 10: METHOD OVERRIDING AND super()
# ============================================================

def practical_10():
    class Animal:
        def sound(self):
            print("Animals make different sounds.")

    class Dog(Animal):
        def sound(self):
            super().sound()
            print("Dog barks.")

    class Cat(Animal):
        def sound(self):
            super().sound()
            print("Cat meows.")

    d1 = Dog()
    d1.sound()

    print()

    c1 = Cat()
    c1.sound()


# ============================================================
# PRACTICAL 11: DESTRUCTOR USING __del__()
# ============================================================

def practical_11():
    class Demo:
        def __init__(self, name):
            self.name = name
            print(
                f"Constructor called: '{self.name}' object created."
            )

        def __del__(self):
            print(
                f"Destructor called: '{self.name}' object destroyed."
            )

    obj = Demo("Sample")
    print("Using the object...")
    del obj
    print("Program continues after deleting object.")


# ============================================================
# PRACTICAL 12: STACK OPERATIONS
# PUSH, POP, PEEK AND SIZE
# ============================================================

def practical_12():
    class Stack:
        def __init__(self):
            self.stack = []

        def push(self, item):
            self.stack.append(item)
            print(f"{item} pushed to stack.")

        def pop(self):
            if not self.stack:
                print("Stack is empty. Cannot pop.")
                return None
            return self.stack.pop()

        def peek(self):
            if not self.stack:
                print("Stack is empty.")
                return None
            return self.stack[-1]

        def size(self):
            return len(self.stack)

    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Peek element:", s.peek())
    print("Popped element:", s.pop())
    print("Stack size:", s.size())


# ============================================================
# PRACTICAL 13: INFIX TO POSTFIX CONVERSION USING A STACK
# ============================================================

def practical_13():
    def precedence(op):
        prec = {
            '+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3
        }
        return prec.get(op, 0)

    def infix_to_postfix(expression):
        stack = []
        result = []

        for ch in expression:
            if ch.isspace():
                continue

            if ch.isalnum():
                result.append(ch)

            elif ch == '(':
                stack.append(ch)

            elif ch == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())

                if not stack:
                    raise ValueError("Mismatched parentheses")

                stack.pop()

            elif ch in '+-*/^':
                while (
                    stack and stack[-1] != '('
                    and (
                        precedence(stack[-1]) > precedence(ch)
                        or (
                            precedence(stack[-1]) == precedence(ch)
                            and ch != '^'
                        )
                    )
                ):
                    result.append(stack.pop())

                stack.append(ch)

            else:
                raise ValueError("Invalid character: " + ch)

        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            result.append(stack.pop())

        return "".join(result)

    expr = "A+B*(C-D)/E"
    print("Infix Expression :", expr)
    print("Postfix Expression:", infix_to_postfix(expr))


# ============================================================
# PRACTICAL 14: POSTFIX TO INFIX CONVERSION USING A STACK
# ============================================================

def practical_14():
    def postfix_to_infix(expression):
        stack = []

        for ch in expression:
            if ch.isspace():
                continue

            if ch.isalnum():
                stack.append(ch)

            elif ch in '+-*/^':
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression")

                op2 = stack.pop()
                op1 = stack.pop()

                combined = "(" + op1 + ch + op2 + ")"
                stack.append(combined)

            else:
                raise ValueError("Invalid character: " + ch)

        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")

        return stack.pop()

    expr = "ABCD-*E/+"
    print("Postfix Expression:", expr)
    print("Infix Expression  :", postfix_to_infix(expr))


# ============================================================
# PRACTICAL 15: QUEUE OPERATIONS
# ENQUEUE, DEQUEUE AND PEEK
# ============================================================

def practical_15():
    class Queue:
        def __init__(self):
            self.queue = []

        def enqueue(self, item):
            self.queue.append(item)
            print(f"{item} enqueued.")

        def dequeue(self):
            if not self.queue:
                print("Queue is empty. Cannot dequeue.")
                return None
            return self.queue.pop(0)

        def peek(self):
            if not self.queue:
                print("Queue is empty.")
                return None
            return self.queue[0]

    q = Queue()
    q.enqueue(5)
    q.enqueue(15)
    q.enqueue(25)
    print("Front element:", q.peek())
    print("Dequeued element:", q.dequeue())
    print("Queue now:", q.queue)


# ============================================================
# PRACTICAL 16: DEQUE INSERTION AND DELETION
# ============================================================

def practical_16():
    dq = deque()

    # Insertion
    dq.append(10)
    dq.append(20)
    dq.appendleft(5)
    print("Deque after insertions:", dq)

    # Deletion
    dq.pop()
    dq.popleft()
    print("Deque after deletions :", dq)


# ============================================================
# PRACTICAL 17: SELECTION SORT
# ============================================================

def practical_17():
    def selection_sort(arr):
        n = len(arr)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

    data = [64, 25, 12, 22, 11]
    print("Original array:", data)
    print("Sorted array  :", selection_sort(data.copy()))


# ============================================================
# PRACTICAL 18: BUBBLE SORT
# ============================================================

def practical_18():
    def bubble_sort(arr):
        n = len(arr)

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", data)
    print("Sorted array  :", bubble_sort(data.copy()))


# ============================================================
# PRACTICAL 19: QUICK SORT
# ============================================================

def practical_19():
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)

    data = [33, 10, 55, 71, 29, 3, 18]
    print("Original array:", data)
    print("Sorted array  :", quick_sort(data))


# ============================================================
# MAIN MENU: SELECT ANY PRACTICAL FROM 1 TO 19
# ============================================================

practicals = {
    1: practical_1,
    2: practical_2,
    3: practical_3,
    4: practical_4,
    5: practical_5,
    6: practical_6,
    7: practical_7,
    8: practical_8,
    9: practical_9,
    10: practical_10,
    11: practical_11,
    12: practical_12,
    13: practical_13,
    14: practical_14,
    15: practical_15,
    16: practical_16,
    17: practical_17,
    18: practical_18,
    19: practical_19
}

while True:
    print("\n========================================")
    print(" OOP WITH PYTHON - PRACTICAL MENU")
    print("========================================")

    print("1. Student Class")
    print("2. Employee getdata() and putdata()")
    print("3. Account and Simple Interest")
    print("4. Student Result and Percentage")
    print("5. Person and Student Inheritance")
    print("6. Multiple Inheritance and Calculator")
    print("7. Person, Employee and Programmer")
    print("8. Customer, Depositor and Borrower")
    print("9. Student, Marks, Sports and Result")
    print("10. Method Overriding and super()")
    print("11. Destructor")
    print("12. Stack Operations")
    print("13. Infix to Postfix")
    print("14. Postfix to Infix")
    print("15. Queue Operations")
    print("16. Deque Operations")
    print("17. Selection Sort")
    print("18. Bubble Sort")
    print("19. Quick Sort")
    print("0. Exit")

    try:
        choice = int(input("Enter practical number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 0:
        print("Program ended.")
        break

    if choice in practicals:
        print("\n--- PRACTICAL", choice, "---")
        try:
            practicals[choice]()
        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)
    else:
        print("Invalid choice. Select a number from 0 to 19.")
