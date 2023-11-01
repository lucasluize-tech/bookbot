def count_words(text):
    return len(text.split())
  
def count_letters(text):
    text = text.lower()
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
path = "books/frankenstein.txt"

with open(path) as file:
    text = file.read()
    word_count = count_words(text)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    for letter, count in count_letters(text).items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
        else: continue
    print(f"--- End report of ---")
    