input_directory = input("Enter directory path: ")
files = os.listdir(input_directory)

if files:
    print("Directory is not empty")
else:
    print("Directory is empty")