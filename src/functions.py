# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if num % 2 == 0:
        print('true')
        return 'true'
    else:
        print('false')
        return 'false'


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def even_odd(cb):
    if cb == 'true':
        print('Even!')
    else:
        print('Odd!')


even_odd(is_even(num))
