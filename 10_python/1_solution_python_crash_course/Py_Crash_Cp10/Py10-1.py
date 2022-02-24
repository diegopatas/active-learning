# Program FILE READER
filename = 'learning_python.txt'

with open(filename) as fo:
    conteudo = fo.read()

print(conteudo)

with open(filename) as fo:
    for line in fo:
        print(line.title())

with open(filename) as fo:
    lines = fo.readlines()

print(lines)
lines.append('Linha nova.')
for i in lines:
    print(i)

stringlines = ''
for i in lines:
    stringlines += i.strip()

print(stringlines)