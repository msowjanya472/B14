get_no_of_words()    
print(data.split())
def get_word_by_initial(letter):
    words = data.split()
    for wd in words:
        if wd.startswith(letter.lower()):
            print(len(wd))
 
    print([wd for wd in words if wd.startswith(letter.lower())])
 




