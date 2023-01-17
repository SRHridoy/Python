with open('file.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    """ The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position """
    f.seek(10)

    # Read the next 5 bytes
    """ The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position """
    print(f.tell())
    data = f.read(5)
    print(data)


""" truncate() function
When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function. """

with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())   