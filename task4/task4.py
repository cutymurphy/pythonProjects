import string

f = open('input04_01.txt', encoding='utf-8', mode='r')
lines = f.readlines()

number = int(lines[0])
text = [word.strip(string.punctuation) for word in lines[1].split()]

words = set()
for word in text:
    if len(word) == number:
        words.add(word)

f = open('output04.txt', encoding='utf-8', mode='w')
for word in words:
    f.write(str(word) + '\n')
