import random
import json
import string

def load_quotes(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def filter_quotes(quotes):
    new_quotes = quotes.copy()
    for i in range(len(quotes)):
        quote = quotes[i]["quote"]
        author = quotes[i]["author"]
        for word in quote.split(" "):
            for char in word:
                if char.isdigit():
                    new_quotes.pop(i)
        quotes[i]["quote"] = quote.upper()
        quotes[i]["author"] = author.upper()
    return new_quotes

def letter_shuffle():
    letters = list(string.ascii_uppercase)
    copy = letters.copy()
    shuffled = {}
    for i in range(26):
        letter = random.choice(copy)
        shuffled[letters[i]] = letter
        copy.remove(letter)
    return shuffled

def combined_quote(quotes):
    quote_num = random.choice(range(0, len(quotes)))
    quote = quotes[quote_num]["quote"]
    author = quotes[quote_num]["author"]
    return quote + " - " + author

def generate_cryptogram():
    quotes = filter_quotes(load_quotes("data/quotes.json")["quotes"])
    shuffled = letter_shuffle()
    solution = combined_quote(quotes)
    solution_list = list(solution)
    for i, char in enumerate(solution_list):
        if char.isalpha():
            solution_list[i] = shuffled[char]
    puzzle = "".join(solution_list)
    return puzzle, solution
    

def main():
    puzzle, solution = generate_cryptogram()
    print(f"PUZZLE: {puzzle}")
    print(f"SOLUTION: {solution}")

if __name__ == "__main__":
    main()