# 1. Open and read a file
# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# 2. Add with keyword
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# 3. When in write mode, you can create a file by typing a file name that does not exist
with open('new_file.txt', mode='w') as file:
    file.write('new file')

