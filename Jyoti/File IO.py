# Reading from file
file=open("Hello.txt") # open a file
text=file.read() # read all text
print(text)
file.close() # close the file


file=open("C:\\Users\\Shailendra\\Desktop\\New Text Document.txt") # open a file
text=file.read() # read all text
print(text)
file.close() # close the file


# Reading line by line
file=open("C:\\Users\\Shailendra\\Desktop\\New Text Document.txt")
for line in file:
    print(line)
file.close()

# Reading line by line
file=open("C:\\Users\\Shailendra\\Desktop\\Text\\New Text Document.txt")
for line in file:
    print(line)
file.close()

# import method
import re
def readline():
    file=open("C:\\Users\\Shailendra\\Desktop\\Text\\New Text Document_jyoti.txt")
    for line in file:
        if (re.search("@gmail.com", line)):
            print(line,end='')
file.close()

# import method
import re
def readline():
    file=open("C:\\Users\\Shailendra\\Desktop\\Text\\New Text Document_jyoti.txt","r")
    file1 = open("C:\\Users\\Shailendra\\Desktop\\Text\\New Text Document_Ram.txt","w")
    for line in file:
        if (re.search("@gmail.com", line)):
            file1.write(line)
            print(line,end='')
file.close()