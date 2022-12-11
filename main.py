from collections import OrderedDict

word = input("Podaj wyraz:\n")

letters = {}

for c in set(word):
    letters[c] = word.count(c)
print(letters, "\n")

letters_2 = OrderedDict(sorted(letters.items()))
print(letters_2, "\n")

backwards = word[::-1]
print(backwards)

