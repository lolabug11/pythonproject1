def is_divisible_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False
def is_number_divisible_by_3(number):
    if number % 3 == 0:
        return True
    else:
        return False
#ask for replacement words and number
def fizz_buzz():
    fizz_replacement= input('What word do you want to use instead of Fizz?\n')
    buzz_replacement= input('What word do you want to use instead of Buzz?\n')
    num = int(input('Enter a number:\n'))
    #check if the number (num) is divisible by 5 or 3
    is_divisible_by_5_v = is_divisible_by_5(num)
    is_number_divisible_by_3_v = is_number_divisible_by_3(num)
    #check what words/combination of words to print
    if is_divisible_by_5_v and is_number_divisible_by_3_v:
        print(f'{fizz_replacement}{buzz_replacement}')
    elif is_number_divisible_by_3_v and not is_divisible_by_5_v:
        print(fizz_replacement)
    elif is_divisible_by_5_v and not is_number_divisible_by_3_v:
        print(buzz_replacement)

