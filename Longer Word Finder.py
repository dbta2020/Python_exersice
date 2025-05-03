words = input("Enter a list of words separated by spaces: ").split()
def longest_word(words):
    longest = ""
    for word in words:
        #We will check only letters, so we will use the isalpha() method to check if the word is a letter
        if not word.isalpha():
            print("Invalid input. Please enter only letters.")
            return None
        if len(word) > len(longest):
            longest = word
    return longest
print("The longest word is:", longest_word(words))
