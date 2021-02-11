import json
from difflib import get_close_matches

file = json.load(open("C:/Users/MY PC/PycharmProjects/data.json"))

def data(word):
    if word.lower() in file:
        return file[word.lower()]
    if word.title() in file:
        return file[word.title()]
    elif word.upper() in file:
        return file[word.upper()]
    elif len(get_close_matches(word, file.keys()))>0:
        x = input("r u looking for '%s' enter Y if yes else N: " %get_close_matches(word,file.keys())[0])
        if x == "Y" or x == 'y':
            return file[get_close_matches(word,file.keys())[0]]
        if x == 'N' or x == 'n':
            return "check ur word and enter again"
        else:
            return "invalid input"
    else:
        return "The word not found"


word = input("enter the Word: ")
output = data(word)
if type(output) == list:
    for i in output:
        print(i)
else:print(output)