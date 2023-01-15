"""(SRH) ----------Opening a File---------- (SRH)"""
'''Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

Here's an example of how to open a file for reading:'''

""" f = open('myFile.txt', 'r')
'''f = open('myFile.txt')#By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.'''
#print(f)
text = f.read()
print(text)
f.close() """

"""(SRH) ----------WRITING TO A FILE---------- (SRH)"""
""" f = open('myfile.txt', 'w')
# f = open('myFile','a') append
f.write('Hello, world!')
f.close() #is must """

'''If we don't want to use f close function then we need to use with and below code:'''

with open('myfile.txt', 'a') as f:
    f.write("Hey, I love OpenCV")









