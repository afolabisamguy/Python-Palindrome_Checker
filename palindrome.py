def palindrome_str():
    word = input('Enter the word you wish to check if it is a palindrome: ')
    if word == word[::-1]:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')


def palindrome_int():
    rev = 0
    while True:
        try:
            digits = int(input('Enter the number you wish to check if it is a palindrome  '))
            break
        except ValueError:
            print('Please enter a valid integer')
    digital = digits
    if digits < 0:
        print(f'{digits} is not a palindrome')
    while digits != 0:
        remainder = digits % 10
        rev = rev * 10 + remainder
        digits = digits // 10

    if rev == digital:
        print(f'{digital} is a palindrome')
    else:
        print(f'{digital} is not a palindrome')


keep_going = True
while keep_going:
    print('Do You Wish to check if a number is a palindrome? or a word is a palindrome?')
    print('If you want to check a number enter "n" otherwise enter "w" to check a word')
    while True:
        answer = input()
        if answer == 'n':
            palindrome_int()
            break
        elif answer == 'w':
            palindrome_str()
            break
        else:
            print('Invalid input! Please try again')
    print('Other words to check?')
    rep = input('Enter Y or N   ')
    if rep.lower() == 'y':
        keep_going = True
    else:
        keep_going = False
