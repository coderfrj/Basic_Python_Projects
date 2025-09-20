from collections import Counter

text = open('text.txt','r')

contents = ''
with text as text:
    contents = text.read()

counter = Counter(contents.split())

print(len(counter))
