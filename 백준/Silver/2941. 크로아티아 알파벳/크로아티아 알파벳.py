alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for a in alphabets:
    word = word.replace(a, ' ')

print(len(word))
