import csv
import os

"""


try:
    f = open('message.txt', 'r')

    # read only the first 6 characters:
    content = f.read(6)
    print(content)

    more_content = f.read(12)
    print(more_content)
finally:
    f.close()


# There is even a better way to write this same code in Python using the with...open syntax.

with open('message.txt', 'r') as f:
    content = f.readlines() # return a list of line with the '\n' spilt
    print(content)

# If you try to open a file that doesn't exist, a new file is automatically created.
# If a file already exists, its contents are removed, and our new content is added to it.

with open('python.txt', 'w') as f:
    f.write("Python is awesome\n")
    f.write("I love Python")

with open('python.txt', 'a') as f:
    f.write("\nPython is my first programming language.")

#print(os.path)
with open('python.txt', 'r') as f:
    lines = f.readlines()
print(lines)
"""

with open('data/test2.csv', 'w') as f:
    header = ['name', 'age', 'email']
    writer = csv.DictWriter(f, fieldnames=header)

    writer.writeheader()
    for i in range(10):
        writer.writerow({'name': f'name{i}', 'age': i * 2, 'email': 'zouhanrui@gmail.com'})
"""
    writer.writerow({'name':'Hanrui', 'age':'27', 'email':'zouhanrui@gmail.com'})
    writer.writerow({'name': 'Hanrui2', 'age': '2', 'email': 'zoanrui@gmail.com'})
    writer.writerow({'name': 'Hanrui3', 'age': '7', 'email': 'zoanrui@gmail.com'})
    writer.writerow({'name': 'Hanrui4', 'age': '272', 'email': 'uhanrui@gmail.com'})

"""
