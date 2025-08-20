from fizz_buzz import *
from palindrone_checker import *
from caesar_cipher import *
if __name__ == "__main__":
    repeat = True
    while repeat == True:
        miny_project_select = input('What project do you want to use?\n1. FizzBuzz\n2. palindrome checker\n')
        if 'fizz' in miny_project_select.lower() or 'buz' in miny_project_select.lower() or '1' in miny_project_select.lower():
            fizz_buzz()
        if 'palindrome' in miny_project_select.lower() or 'checker' in miny_project_select.lower() or '2' in miny_project_select.lower():
            palindrome_checker()
        repeat = bool(input('Do you want to repeat (True or False, this is case sensitive)?\n'))