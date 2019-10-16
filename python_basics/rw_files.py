# read all contents from file with context manager 
with open('test.txt', 'r') as file: # where file is the file object
    f_contents = file.read()

print(f_contents)

# read all contents into a list
with open('test.txt', 'r') as file:
    f_contents = file.readlines()
    print(f_contents, end='')

# read one line at a time
with open('test.txt', 'r') as file:
    f_contents = file.readline()
    print(f_contents, end='')

    f_contents = file.readline()
    print(f_contents)

# use read to get specified number of chars
with open('test.txt', 'r') as file:
    print(file.read(10))
    print(file.tell()) # gives the current position of the cursor

# read lines from large file without running out of memory
# just iterate over it

# first line by line
with open('test.txt', 'r') as file:
    for line in file: # iterate over the file object
        print(line, end='')

# using specified number of chars
with open('test.txt', 'r') as file:
    chars_to_read = 5
    
    f_contents = file.read(chars_to_read)
    print(f_contents, end='|')

    while len(f_contents) > 0:
        print(f_contents, end='|')
        f_contents = file.read(chars_to_read)        

# changing the current position of the cursor
with open('test.txt', 'r') as file:
    chars_to_read = 5
    
    f_contents = file.read(chars_to_read)
    print(f_contents, end='|')

    file.seek(0)  # change the cursor position

    f_contents = file.read(chars_to_read)
    print(f_contents, end='|')

# writing to file with w mode (but if file exists it overwrites it, use a for append mode)
with open('test2.txt', 'w') as file:
    file.write('hello world') 
    # can use seek here to overwrite the data as well and the write also follows the current 
    # position to write as well


# read from file and write to another
with open('test.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# another more effiecient way is to read and write in chunks
with open('test.txt', 'r') as rf:
    with open('test2.txt', 'a') as wf:
        chunk_size = 5
        
        rf_content = rf.read(chunk_size)
        while len(rf_content) > 0:
            wf.write(rf_content)
            rf_content = rf.read(chunk_size)

# lets try to open image file in binary format
with open('dogo.jpg', 'rb') as file: # where b argument specifies the binary format
    print(file.read())


