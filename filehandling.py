
FILE_PATH = r"c:\Users\Murali\New folder\Python\kritiksha.txt"
f = open(FILE_PATH, "r")
print(dir(f))
content = f.readlines()
print(len(content))

data= f.read()

def get_no_of_words(): 
    print(len(data.split()))


get_no_of_words()    
print(data.split())
def get_word_by_initial(letter):
    words = data.split()
    for wd in words:
        if wd.startswith(letter.lower()):
            print(len(wd))
 
    print([wd for wd in words if wd.startswith(letter.lower())])
 



get_word_by_initial("a")
def get_word_len_map():
    words = data.split()
    d = {}
    for wd in words:
        d[wd] = len(wd)
    print(d)    
    



def get_total_char():
    print(len(data))#d#d#d





data = f.read()
data2 = f.readline(3)
print(data)
data= f.read()
print(data)
print(content)



import re


para = "Hello!!! Welcome to Python's world... #1 programming language @2025."
#Remove special characters (keep only letters, numbers, and spaces)
data = re.sub(r'[^A-Za-z0-9\s]', '', para)

print("Original Paragraph:")
print(data)
print("\nCleaned Paragraph:")
print(para)

import re
FILE_PATH = r"c:\Users\Murali\New folder\Python\kritiksha.txt"
f = open(FILE_PATH, "r")

Content= f.read()
#
# Open the input file in read mode
with open("input.txt", "r") as f:
    paragraph = f.read()
   
# Remove numbers and special characters (keep only letters and spaces)
cleaned_paragraph = re.sub(r'[^A-Za-z\s]', '', paragraph)

# Open the output file in write mode
with open("output.txt", "w") as f:
    f.write(cleaned_paragraph)

print("Cleaning completed. Check 'output.txt'.")




