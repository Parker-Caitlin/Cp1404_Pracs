"""
CP1404- Prac
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Please enter a number"))
        finished = True
        pass
    except  ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)