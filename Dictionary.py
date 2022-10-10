import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(d):
    
    d = d.lower()
    
    if d in data :
        return data[d]
    elif len(get_close_matches(d,data.keys())) > 0 :
        yn = input("Did you mean % s instead? Enter Y if yes , or N if no: "%get_close_matches(d,data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(d,data.keys())]
        elif yn == "n":
            return "The word does not exist. Please double check it"
        else:
            return "The word does not exist . Please double check it."

word = input("Enter a word! : ")
output = translate(word)

if type(output) == list:
     for item in output:
         print(item)
else:
    print(output)
input("Press ENTER to exit.")
