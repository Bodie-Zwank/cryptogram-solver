import math
from generator import generate_cryptogram

def load_dictionary(file_path):
    with open(file_path, 'r') as f:
        return set(word.strip() for word in f)
    
dictionary = load_dictionary("dictionary.txt")

def main():
    puzzle, solution = generate_cryptogram()
    print(puzzle, solution)


if __name__ == "__main__":
    main()