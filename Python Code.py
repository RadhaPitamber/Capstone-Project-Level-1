# Get user information
name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid age.")

house_number = ""

while not house_number:
    house_number = input("Enter your house number: ")
    if not house_number:
        print("Please enter a valid house number.")

street_name = input("Enter your street name: ")

# Print out user details in a single sentence
print(f"{name} is {age} years old, living at {house_number} on {street_name} street.")

