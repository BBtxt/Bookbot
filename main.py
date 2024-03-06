def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    num_words = word_count(text)
    num_letters = count_letters(text)
    aggregate_letters(num_letters)

def read_book(book_path):
    with open(book_path, "r") as file:
        text = file.read()
    return text

def word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    

def aggregate_letters(chars):
    chars = dict(sorted(chars.items()))
    for key in chars: 
        if key.isalpha():
            print(f'The "{key}" character was found {chars[key]} times')
main()