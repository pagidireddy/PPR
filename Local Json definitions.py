import json
from difflib import get_close_matches
file = json.load(open("C:/Users/MY PC/Downloads/data.json"))


def defination(word):
    if word.lower() in file:
        return file[word.lower()]
    elif word.title() in file:
        return file[word.title()]
    elif word.upper() in file:
        return file[word.upper()]
    elif len(get_close_matches(word,file.keys()))>0:
        new_word = input("are you looking for %s Enter 'Y' if yes or 'N' if no?" %get_close_matches(word,file.keys())[0])
        if new_word == 'Y' or new_word =="y":
            return file[get_close_matches(word,file.keys())[0]]
        elif new_word == "N" or new_word == 'n':
            return "the Word not found"
        else :
            return "enter valid input"
    else:
        print("No Definition fond,Kindly recheck ur word")


word= input("Enter ur Word: ")
out = defination(word)
if type(out) == list:
    for item in out:
        print(item)
else:
    print(out)