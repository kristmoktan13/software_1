gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")
else:
    print("Invalid gender.")

