# Steve Stylin, Module 1.3 Assignment, 10/26/2024
print("\n Steve Stylin, Module 1.3 Assignment, 10/26/2024\n ")
    
def countdown_bottles(num_bottles):
    # Loop from the number of bottles down to 1
    for i in range(num_bottles, 0, -1):
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.\n")
            print("Take one down, pass it around, 0 bottles of beer on the wall.\n")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\n")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")
    
   

def main():
    while True:
        try:
            # Ask the user for the number of bottles
            user_input = int(input("How many bottles of beer are on the wall? \n"))
            if user_input <= 0:
                print("Please enter a positive integer.\n")
                continue
            # Call the countdown function
            countdown_bottles(user_input)
            break  # Exit the loop after successful countdown
        except ValueError:
            print("Invalid input. Please enter a positive integer.\n")

    # Remind the user to buy more beer
    print("Don't forget to buy more beer!\n")
    exit(0)  # Terminate the program with exit code 0

# Run the main function
if __name__ == "__main__":
    main()
