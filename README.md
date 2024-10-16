# Python-Palindrome_Checker

This Python script allows users to check if a given word or number is a palindrome. A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward.

## Features

- Check if a word is a palindrome
- Check if a number is a palindrome
- User-friendly command-line interface
- Input validation for number checking
- Option to continue checking multiple inputs

## How to Use

1. Run the script in a Python environment.
2. Choose whether you want to check a word or a number:
   - Enter 'w' to check a word
   - Enter 'n' to check a number
3. Follow the prompts to enter your word or number.
4. The program will display whether the input is a palindrome or not.
5. You can choose to check another input or exit the program.

## Functions

### `palindrome_str()`

This function checks if a given word is a palindrome:
- Prompts the user to enter a word
- Compares the word with its reverse
- Prints whether the word is a palindrome or not

### `palindrome_int()`

This function checks if a given number is a palindrome:
- Prompts the user to enter a number
- Handles input validation to ensure a valid integer is entered
- Reverses the digits of the number
- Compares the original number with its reverse
- Prints whether the number is a palindrome or not

## Main Loop

The main loop of the program:
- Asks the user to choose between checking a word or a number
- Calls the appropriate function based on the user's choice
- Allows the user to continue checking multiple inputs or exit the program

## Notes

- Negative numbers are automatically considered not palindromes.
- The program will continue running until the user chooses to exit.

Feel free to modify or extend this script to add more features or improve its functionality!
