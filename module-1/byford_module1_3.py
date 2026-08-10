# Armond Drew Byford
# August 10, 2026
# CSD-325 Advanced Python
# Module 1.3 - On the Wall
# Purpose: Count down the bottles of beer on the wall based on user input.


# Function that manages the bottle countdown
def countdown(bottles):
    """Count down the bottles of beer on the wall."""

    # Count backward while there is more than one bottle
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall,")
        print(f"{bottles} bottles of beer.")
        print("Take one down and pass it around.")

        bottles = bottles - 1

        # Use the correct singular or plural wording
        if bottles == 1:
            print("1 bottle of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall.\n")

    # Display the final verse using the singular word "bottle"
    print("1 bottle of beer on the wall,")
    print("1 bottle of beer.")
    print("Take one down and pass it around.")
    print("No more bottles of beer on the wall.\n")


# Main program - continue asking until the user enters valid input
while True:
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))

        # Make sure the number of bottles is greater than zero
        if bottles > 0:
            break

        print("Please enter a number greater than 0.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


# Pass the valid number of bottles to the countdown function
countdown(bottles)

# Remind the user to buy more beer after the countdown is complete
print("Time to buy more beer!")