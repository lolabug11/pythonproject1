from fizz_buzz import *
from palindrone_checker import *
from caesar_cipher import *
from word_frequincy_counter import *
from bank import *
if __name__ == "__main__":
    repeat = 'y'
    while 'y' in repeat:
        miny_project_select = input('What project do you want to use?\n1. FizzBuzz\n2. palindrome checker\n3. caesar cypher\n4. word frequency counter\n5. Banking\n')
        if 'fizz' in miny_project_select.lower() or 'buz' in miny_project_select.lower() or '1' in miny_project_select.lower():
            fizz_buzz()
        if 'palindrome' in miny_project_select.lower() or 'checker' in miny_project_select.lower() or '2' in miny_project_select.lower():
            palindrome_checker()
        if 'caeser' in miny_project_select.lower() or 'cypher' in miny_project_select.lower() or '3' in miny_project_select.lower():
            caesar_cypher()
        if 'word' in miny_project_select.lower() or "frequency" in miny_project_select.lower() or 'counter' in miny_project_select.lower() or '4' in miny_project_select.lower():
            word_frequincy_counter()
        if 'banking' in miny_project_select.lower() or '5' in miny_project_select.lower():
            banking()
        repeat = input('Do you want to repeat (yes or no)?\n')