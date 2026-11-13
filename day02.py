name="naveen"
day= 2
print(name, "is on day", day)

words=["git", "push", "git", "commit"]
print(words[0])
print(len(words))

counts={"git":2, "push":1}
print(counts["push"])

text=open("notes.txt").read()
words = text.split()
print("total words:", len(words))

counts= {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)