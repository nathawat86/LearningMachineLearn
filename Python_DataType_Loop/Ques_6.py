# Accept an English alphabet from the user
alphabet = input("Enter an English alphabet: ")

# Convert the input to lowercase if it's a capital letter
alphabet = alphabet.lower()

# Check if the alphabet is a consonant or a vowel
if alphabet.isalpha() and len(alphabet) == 1:
    if alphabet in 'aeiou':
        print(alphabet, " is a vowel.")
    else:
        print(alphabet, "is a consonant.")
else:
    print(alphabet, " in invalid input. Please enter a single English alphabet.")
