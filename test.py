counts = {"git":2}
print(counts.get("git",0))
print(counts.get("push",0))
print(counts.get("push",99))
print(counts.get("git",0)+1)

def clean_word(word):
    word = word.lower()
    word = word.strip(".,!?#$%")
    return word 
messy = ["RAMA", "Sita", "LaKsHma", "Bartha@", "hanuma@$%"]
for w in messy:
    print(clean_word(w))