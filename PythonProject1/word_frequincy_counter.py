def count_frequency(string):
    orig_string = string
    string += ' '
    string = string.lower()
    words = {}
    current_word = ''
    for char in string:
        if char.isalpha():
            current_word += char
        else:
            if current_word in words:
                words[current_word] += 1
            elif current_word not in words:
                words[current_word] = 1
            current_word = ''
    most_repeated_word = max(words, key=lambda key: words[key])
    amount_of_times_most_repeated_word_is_said = max(words.values())
    print(f'The most repeated word in the sentance "{orig_string}" is "{most_repeated_word}". "{most_repeated_word}" was repeated {amount_of_times_most_repeated_word_is_said} times.')
def word_frequincy_counter():
    string = input('What sentance do you want to see the most frequent word?\n')
    count_frequency(string)
