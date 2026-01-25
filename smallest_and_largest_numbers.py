smallest = None
largest = None
while True:
    value = input("Enter a number (empty to quit): ")
    if value == "":
        break
    number = float(value)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
print("Smallest number:", smallest)
print("Largest number:", largest)
