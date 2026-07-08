#  file handling means reading from or writing to files -- like opening anotebook, writing in it, or reading it. 
# In Python, we can handle files using built-in functions and methods.
#  'r' - read(default), 'w' - write(overwrites), 'a' - append(add at end), 'x' - create new file(error if exists), 'r+' - read and write.
#.ipynb - jupiter file extension

file_path = 'example.txt'

# 1. Write to a file using 'w' mode
# Command: python file-handling.py
with open(file_path, 'w') as file:
    file.write('Hello, beginner!\n')
    file.write('This is a simple file-handling example.\n')

print('Step 1: Written to example.txt using write mode (w).')

# 2. Read from the file using 'r' mode
with open(file_path, 'r') as file:
    content = file.read()

print('\nStep 2: Read from example.txt using read mode (r):')
print(content)

# 3. Append text to the file using 'a' mode
with open(file_path, 'a') as file:
    file.write('Appending one more line.\n')

print('Step 3: Appended a new line using append mode (a).')

# 4. Read again to show the updated file content
with open(file_path, 'r') as file:
    updated_content = file.read()

print('\nStep 4: Read updated content from example.txt:')
print(updated_content)

# Notes on file modes:
# 'r'  = read only
# 'w'  = write only (creates file or truncates existing file)
# 'a'  = append only (adds content to end of file)
# 'x'  = create new file, fails if file exists
# 'r+' = read and write

# Example terminal commands:
# python file-handling.py   # run this script
# type example.txt         # on Windows, show file content in terminal
# cat example.txt          # on macOS/Linux, show file content
