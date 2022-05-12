#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: May 2022
# This program lets the user input numbers and get the largest and smallest


def main():
    # this function lets the user input numbers and get the largest and smallest

    # input
    numberList = []
    while True:
        integer = input("Enter your number to the List: ")
        try:
            integer_int = int(integer)
            numberList.append(integer_int)
            finish = input("\nWould you like to end? (Enter yes or no): ")
            # process
            if finish == "yes":
                print("")
                break
            elif finish == "no":
                print("")
                continue
            else:
                print("\nPlease enter yes or no next time\n")
        except Exception:
            print("\nThis was not an integer\n")
    # output
    print("\nThe largest number is:", max(numberList))
    print("\nThe smallest number is:", min(numberList))


if __name__ == "__main__":
    main()
