def single_word_checker(word):
    word_as_list = []
    reversed_word = ''
    for char in word:
        word_as_list.append(char)
    for i in range(len(word)):
        reversed_word+=word_as_list[(-i)-1]
    if reversed_word == word:
        print(f'{word} is a palindrome.')
    else:
        print(f'{word} is not a palindrome.')
        print(f'{word} reversed is {reversed_word}.')
def number_checker(number):
    number = str(number)
    number_as_list = []
    reversed_number = ''
    for digit in number:
        number_as_list.append(digit)
    for i in range(len(number)):
        reversed_number+=number_as_list[(-i)-1]
    if number == reversed_number:
        print(f'{number} is a palindrome.')
    else:
        print(f'{number} is not a palindrome.')
        print(f'{number} reversed is {reversed_number}.')
def sentence_checker(sentence):
    sentence_as_list = []
    sentence_without_punctuation_or_white_space = ''
    reversed_sentence = ''
    for  char in sentence:
        if char == '.' or char == ' ':
            _ = char
        else:
            sentence_without_punctuation_or_white_space += char
            sentence_as_list.append(char)
    for i in range(len(sentence_as_list)):
        reversed_sentence += sentence_as_list[(-i) - 1]
    if sentence_without_punctuation_or_white_space == reversed_sentence:
        print(f'{sentence} (without punctuation or white space) is a palindrome.')
    else:
        print(f'{sentence} is not a palindrome.')
def palindrome_checker():
    type_of_palindrome_checker = input('What do you want to check to be a palindrome?\n1. single word\n2. number\n3. sentence\n')
    if 'single' in type_of_palindrome_checker.lower() or 'word' in type_of_palindrome_checker.lower() or '1' in type_of_palindrome_checker.lower():
        word = input('what word do you want to check?\n')
        single_word_checker(word)
    elif 'number' in type_of_palindrome_checker.lower() or '2' in type_of_palindrome_checker.lower():
        number = int(input('What integer do you want to check?\n'))
        number_checker(number)
    elif 'sentence' in type_of_palindrome_checker.lower() or '3' in type_of_palindrome_checker.lower():
        sentence = input('What sentence do you want to check?\n')
        sentence_checker(sentence.lower())
