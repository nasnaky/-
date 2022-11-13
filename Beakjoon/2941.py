stre = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in stre:
    word = word.replace(i, '*')
print(len(word))