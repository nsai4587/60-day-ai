counts = {"git":2}
print(counts.get("git",0))
print(counts.get("push",0))
print(counts.get("push",99))
print(counts.get("git",0)+1)