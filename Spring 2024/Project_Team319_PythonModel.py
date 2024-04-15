global angle
global idist
global fdist
global error


def calculate_deviation(angle, idist, fdist):
    """Calculate deviation based on the angle, initial distance, and final distance."""
    # These error values are taken from the test data of the robot. Excel analysis is used to find these values.
    # These values are then used to calculate the deviation.
    # This if else ladder ensures that the user input is limited and thus the robot runs smoothly and efficiently.

    if angle == "l90":
       if 0 < idist <= 12:
          error = (fdist / 12) * 0.033867
       elif 12 < idist <= 24:
          error = (fdist / 12) * 0.08943
       elif 24 < idist <= 48:
          error = (fdist / 12) * 0.073232
       elif 48 < idist <= 96:
          error = (fdist / 12) * 0.19724
       else:
          print("Invalid initial distance. Please enter a valid value.")
          return None
       return error
    elif angle == "r90":
       if 0 < idist <= 12:
          error = (fdist / 12) * 0.033867
       elif 12 < idist <= 24:
          error = (fdist / 12) * 0.08943
       elif 24 < idist <= 48:
          error = (fdist / 12) * 0.073232
       elif 48 < idist <= 96:
          error = (fdist / 12) * 0.19724
       else:
          print("Invalid initial distance. Please enter a valid value.")
          return None
       return error

# Function display_deviation is used to display the deviation.
# This function takes the error as a parameter input and displays it.

def display_deviation(error):
    """Display the calculated deviation."""
    if error is not None:
       print("The robot deviates to the right by: ", error)


# Taking the input from the user and calling the calculate_deviation function..
"""Main function to execute the program."""

angle = input("Enter the angle (l90/r90): ")
idist = int(input("Enter the initial distance (in): "))
fdist = int(input("Enter the final distance (in): "))

error = calculate_deviation(angle, idist, fdist)
display_deviation(error)