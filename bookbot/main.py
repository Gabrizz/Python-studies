def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  # print(text)
  print(f"--- Begin report of {book_path} ---")
  print(f"{get_number_of_words(text)} words found in the document")
  print("Each letter appears:")
  characters_count = get_characters_count(text)
  characters_count_list = list(characters_count)
  for i in range(26):
    print(f"'{characters_count_list[i]}': {characters_count[characters_count_list[i]]}")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_number_of_words(text):
  words = text.split()
  return len(words)

def get_characters_count(text):
  characters_dictionary = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
    'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
    'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '0': 0, '1': 0,
    '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0,
    '9': 0, '.': 0, ':': 0, ',': 0, ';': 0, '-': 0, '_': 0,
    '(': 0, ')': 0, '[': 0, ']': 0, "'": 0, '"': 0, '*': 0,
    '$': 0, '@': 0, '#': 0, '%': 0, '/': 0, '?': 0, '!': 0,
    ' ': 0, '\n': 0
  }
  for i in range(len(text)):
    lowered = text[i].lower()
    if lowered in characters_dictionary:
      characters_dictionary[lowered] += 1
    else:
      characters_dictionary[lowered] = 1
  return characters_dictionary

main()