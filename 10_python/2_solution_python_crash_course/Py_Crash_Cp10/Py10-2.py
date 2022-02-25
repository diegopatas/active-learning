filename = 'learning_python.txt'

with open(filename) as fileobj:
    content = fileobj.read()
    print(f"The reading step is complete!")
    for i in content:
        i.replace('python', 'C')

print(content)