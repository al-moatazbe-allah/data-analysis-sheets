#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Print each word individually from a string
def print_words(sentence):
    words = sentence.split()
    for word in words:
        print(word)

sentence = input("Enter a sentence: ")
print_words(sentence)

# 2. Concatenate two strings
def ConCate():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    return str1 +" "+ str2

print(ConCate())

# 3. Perform mathematical operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
print(calculate(num1, num2, operator))

# 4. Edit a tuple
def edit_tuple(tup, index, new_value):
    lst = list(tup)
    lst[index] = new_value
    return tuple(lst)

tup = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
index = int(input("Enter index to edit: "))
new_value = int(input("Enter new value: "))
print(edit_tuple(tup, index, new_value))

# 5. Concatenate integer and string
def concat_int_string():
    num = input("Enter an integer: ")
    text = input("Enter a string: ")
    print(str(num) + text)

concat_int_string()

# 6. Remove first and last characters from a string
def remove_first_last(string):
    return string[1:-1]

string = input("Enter a string: ")
print(remove_first_last(string))

# 7. Print even numbers (two ways)
def print_evens(n):
    print([i for i in range(n) if i % 2 == 0])

def print_evens_loop(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)

n = int(input("Enter a number: "))
print_evens(n)
print_evens_loop(n)

# 8. Print star pattern
def star_pattern(rows):
    for i in range(1, rows+1):
        print('*' * i)

rows = int(input("Enter number of rows: "))
star_pattern(rows)

# 9. Calculate distance between two points
def distance_2D(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5

x1, y1 = map(int, input("Enter first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter second point (x2 y2): ").split())
print(distance_2D((x1, y1), (x2, y2)))

# 10. Matrix statistics import numpy as np
def matrix_statistics():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        matrix.append([int(x) for x in input().split()])
    arr = np.array(matrix)
    print("Mean:", np.mean(arr, axis=0))
    print("Std Dev:", np.std(arr, axis=0))
    print("Variance:", np.var(arr, axis=0))
    print("Median:", np.median(arr, axis=0))
    print("Quantiles:", np.quantile(arr, [0.25, 0.5, 0.75], axis=0))
    print("Column Sum:", np.sum(arr, axis=0))

# Uncomment to run the function
# matrix_statistics()

# 11. Remove all 'C' characters from a string
def remove_C(sentence):
    return sentence.replace('C', '').replace('c', '')

sentence = input("Enter a sentence: ")
print(remove_C(sentence))

# 12. Class for statistical calculations
import numpy as np
class Statistics:
    def __init__(self, data):
        self.data = np.array(data)
    
    def mean(self):
        return np.mean(self.data)
    
    def std_dev(self):
        return np.std(self.data)
    
    def variance(self):
        return np.var(self.data)
    
    def median(self):
        return np.median(self.data)

# Example usage
stats = Statistics([1, 2, 3, 4, 5, 6])
print("Mean:", stats.mean())
print("Std Dev:", stats.std_dev())
print("Variance:", stats.variance())
print("Median:", stats.median())


# In[ ]:





# In[ ]:




