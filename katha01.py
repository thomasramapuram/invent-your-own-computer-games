alpha = 'abcdefghijklmnopqrstuvwxyz'
text = "The narwhal bacons at midnight."
text = text.lower()
rv = []
for i in text:
    if i in alpha:
        rv.append(alpha.index(i)+1)
print(' '.join(map(str, rv)))
x = (str(ord(c) - 96) for c in text.lower())