# write a file 
with open ("diary.txt", "w") as f:
    f.write("Day 4: I am learning files. \n")
    f.write("I showed up again on day 4.\n")

# read it back  cv
with open( "diary.txt", "r") as f:
    text= f.read()
    
print(text)

import json
notes = [
    {"day":1, "topic": "git"}, 
    {"day":2, "topic": "lists and dictionaries"}, 
    {"day":3, "topic": "functions"}, 
    {"day":4, "topic": "files and json"}
     
]
# save the list to a file 
with open("notes.json", "w")as f:
    json.dump(notes, f, indent=2)
    
# load it back 
with open("notes.json", "r") as f:
    loaded= json.load(f)
    
print(loaded[0]["topic"])
print(len(loaded))
    
