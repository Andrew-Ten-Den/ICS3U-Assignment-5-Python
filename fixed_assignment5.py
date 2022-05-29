#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: April 2022
# This finds the largest and smallest numbers


def main():
    # this function finds the largest and smallest numbers

    counter = 1
    biggest = 0
    smallest = 0

    # input
    amount = input("Enter how many numbers you will input (ex: 4): ")
    try:
        amount_int = int(amount)
        print("")
        # process & output
        starting = input("Enter an integer: ")
        try:
            starting_int = int(starting)
            biggest = starting_int
            smallest = starting_int
            while amount_int > counter:
                integer = input("Enter an integer: ")
                try:
                    integer_int = int(integer)
                    counter = counter + 1

                    if integer_int > biggest:
                        biggest = integer_int

                    elif integer_int < smallest:
                        smallest = integer_int

                except Exception:
                    print("\nThis was not an integer")

            print("\nThe largest integer is {}".format(biggest))
            print("\nThe smallest integer is {}".format(smallest))

        except Exception:
            print("\nThis was not an integer")
    except Exception:
        print("\nThis was not an integer")

    print("\nDone")


if __name__ == "__main__":
    main()
