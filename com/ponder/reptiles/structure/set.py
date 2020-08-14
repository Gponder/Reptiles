v = {"abc", 1, 'a'}
print(type(v))
v = set()
print(type(v))
v.add("c")
v.add(1)
print("c" in v)
for o in v:
    print(o)
v.add("cc")
