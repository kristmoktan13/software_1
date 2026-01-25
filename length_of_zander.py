length=int(input("Enter the length of the zander in centimetre: "))
if length<42:
    print("Release the fish back into the lake.")
    print("The fish is",42-length,"centimetres below the size limit.")
else:
    print("The zander meets the size limit.")
