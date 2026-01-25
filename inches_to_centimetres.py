while True:
    inches = float(input("Enter in inches (no negative values): "))

    if inches < 0:
        break

    centimeters = inches * 2.54
    print(centimeters, "cm")
