# While loop
counter = 1
print("While Loop Output:")
while counter <= 3:
    print(f"Count: {counter}")
    counter += 1

# Do-while equivalent in Python
print("\nDo-While Loop Output:")
number = 0
while True:
    print(f"Number is {number}")
    number += 1
    if number >= 3:
        break
