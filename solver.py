import math
from generator import generate_cryptogram

def load_dictionary(file_path):
    with open(file_path, 'r') as f:
        return set(word.strip() for word in f)

def load_word_shapes(file_path):
    pass

def word_shape(word):
    word_shape = []
    num = 0
    char_nums = {}
    for i, char in enumerate(word):
        if char in char_nums:
            word_shape.append(char_nums[char])
        else:
            word_shape.append(num)
            char_nums[char] = num
            num += 1
    return "".join(map(str, word_shape))

def sort(puzzle):
    # sorts longest to shortest so that longest word can be processed first
    for i in range(len(puzzle)):
        for j in range(len(puzzle) - i - 1):
            if len(puzzle[i]) < len(puzzle[j]):
                puzzle[i], puzzle[j] = puzzle[j], puzzle[i]
    return puzzle

def main():
    dictionary = load_dictionary("data/dictionary.txt")
    puzzle, solution = generate_cryptogram()
    sorted_puzle = sort(puzzle)
    shape = word_shape()


if __name__ == "__main__":
    main()