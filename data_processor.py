from solver import load_dictionary, word_shape


dictionary = load_dictionary("data/dictionary.txt")

f = open("data/word_shapes.txt", "w")

for word in dictionary:
    shape = word_shape(word)
    f.write(shape + "\n")

f.close()