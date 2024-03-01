#!/usr/bin/env python3

# quiz 1
def greet_programmer():
    
    print("Hello, programmer!")

# quiz 2
def greet(name):
    
    return ("hello, {name}!")

greet("Naureen")

# quiz 3
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Sunny")

# quiz 4
def add(num1, num2):
    sum = num1 + num2
    return sum

result = add(8, 10)
print(result)

# quiz 5
def halve(number):
      if type(number) in (int, float):
        return number / 2
      else:
        return None

result = halve(4)
print(result)

result = halve("two")
print(result)
