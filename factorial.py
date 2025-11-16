#!/usr/bin/env python3

# Created By: Brandon
# Date: November 16th, 2025
# This program asks the user for the number and then calculates the factorial


def main():

    # get the age from the user
    number = input("Enter a positive number: ")

    # initialize counter and sum
    counter = 0
    factorial = 1

    # Checking if the user entered an integer correctly
    try:

        number = int(number)
        print("You entered an integer!")

        # determine whether or the not the number is positive
        if number < 0:
            print("Please Enter a positive number")
        else:
            while True:
                counter = counter + 1
                factorial = factorial * counter
                print("Tracking Counter {} ".format(counter))
                if counter >= number:
                    break

            print("")
            print("{}! = {}".format(number, factorial))

    except ValueError:
        print("That is not a valid integer")


# outputs the function
if __name__ == "__main__":
    main()
